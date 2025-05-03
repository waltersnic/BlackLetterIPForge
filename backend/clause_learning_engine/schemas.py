from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# User input schema
class UserCreate(BaseModel):
    username: str
    password: str

# Token response
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

# Token payload
class TokenData(BaseModel):
    username: Optional[str] = None

# Clause input schema
class ClauseInput(BaseModel):
    clause_id: Optional[str] = None
    user_id: str
    title: str
    content: str
    document_type: str
    jurisdiction: Optional[str] = "US"
    edited: bool = False
    accepted: bool = False

# User output
class UserOut(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True
