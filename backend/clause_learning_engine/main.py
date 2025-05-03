from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
from uuid import uuid4
from datetime import datetime

from .db import SessionLocal, engine, Base
from .models import Clause
from sqlalchemy.orm import Session

app = FastAPI(
    title="Clause Learning Engine API",
    description="Receives contract clauses, parses redline behavior, and stores edits.",
    version="0.2.0"
)

# Create tables
Base.metadata.create_all(bind=engine)

# Dependency for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class ClauseInput(BaseModel):
    clause_id: Optional[str] = None
    user_id: str
    title: str
    content: str
    document_type: str
    jurisdiction: Optional[str] = "US"
    edited: bool = False
    accepted: bool = False

@app.get("/")
def root():
    return {"message": "Clause Learning Engine with SQLite is running."}

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
