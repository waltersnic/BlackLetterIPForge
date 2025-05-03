from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from uuid import uuid4
from datetime import datetime

app = FastAPI(
    title="Clause Learning Engine API",
    description="Receives contract clauses, parses redline behavior, and simulates feedback tracking.",
    version="0.1.0"
)

# Simulated in-memory clause database
clause_db = []

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
    return {"message": "Clause Learning Engine is running."}

@app.post("/clause/submit")
def submit_clause(input: ClauseInput):
    clause_id = input.clause_id or str(uuid4())
    record = {
        "clause_id": clause_id,
        "user_id": input.user_id,
        "title": input.title,
        "content": input.content,
        "doc_type": input.document_type,
        "jurisdiction": input.jurisdiction,
        "edited": input.edited,
        "accepted": input.accepted,
        "timestamp": datetime.utcnow().isoformat()
    }
    clause_db.append(record)
    return {"status": "stored", "clause_id": clause_id}

@app.get("/clauses/{user_id}")
def get_user_clauses(user_id: str):
    user_clauses = [c for c in clause_db if c["user_id"] == user_id]
    return {"clauses": user_clauses}

@app.get("/clause/{clause_id}")
def get_clause_by_id(clause_id: str):
    match = next((c for c in clause_db if c["clause_id"] == clause_id), None)
    if not match:
        raise HTTPException(status_code=404, detail="Clause not found")
    return match
