# Clause Learning Engine (Backend)

This is the FastAPI backend for Blackletter IP Forge's Clause Learning Engine.

## Features
- Accepts and stores clauses submitted by users
- Tracks whether a clause was accepted or edited
- Simulates clause learning loop
- Returns clauses by user ID or clause ID

## Endpoints
- `POST /clause/submit` – Submit a clause with metadata
- `GET /clauses/{user_id}` – View all clauses for a user
- `GET /clause/{clause_id}` – Get a specific clause by ID

## Getting Started (Local)
```bash
pip install -r requirements.txt
uvicorn main:app --reload
