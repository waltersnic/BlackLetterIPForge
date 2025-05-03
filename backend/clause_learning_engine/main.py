from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from uuid import uuid4
from .db import SessionLocal, engine, Base
from .models import Clause, User
from .schemas import ClauseInput, UserCreate, Token, UserOut
from .auth import (
    hash_password, verify_password,
    create_access_token, decode_access_token
)
from datetime import datetime, timedelta

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Clause Learning Engine + Auth", version="0.3.0")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Auth helper
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = db.query(User).filter(User.username == payload.get("sub")).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(status_code=400, detail="Username already exists")
    hashed = hash_password(user.password)
    new_user = User(username=user.username, hashed_password=hashed)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/me", response_model=UserOut)
def read_me(current_user: User = Depends(get_current_user)):
    return current_user

@app.post("/clause/submit")
def submit_clause(input: ClauseInput, db: Session = Depends(get_db)):
    clause = Clause(
        clause_id=input.clause_id or str(uuid4()),
        user_id=input.user_id,
        title=input.title,
        content=input.content,
        document_type=input.document_type,
        jurisdiction=input.jurisdiction,
        edited=input.edited,
        accepted=input.accepted
    )
    db.add(clause)
    db.commit()
    return {"status": "stored", "clause_id": clause.clause_id}

@app.get("/clauses/{user_id}")
def get_user_clauses(user_id: str, db: Session = Depends(get_db)):
    return db.query(Clause).filter(Clause.user_id == user_id).all()

@app.get("/clause/{clause_id}")
def get_clause_by_id(clause_id: str, db: Session = Depends(get_db)):
    clause = db.query(Clause).filter(Clause.clause_id == clause_id).first()
    if clause is None:
        raise HTTPException(status_code=404, detail="Clause not found")
    return clause
