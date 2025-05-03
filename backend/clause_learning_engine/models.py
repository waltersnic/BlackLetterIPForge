from sqlalchemy import Column, String, Boolean, DateTime, Integer
from datetime import datetime
from .db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class Clause(Base):
    __tablename__ = "clauses"

    clause_id = Column(String, primary_key=True, index=True)
    user_id = Column(String)
    title = Column(String)
    content = Column(String)
    document_type = Column(String)
    jurisdiction = Column(String)
    edited = Column(Boolean)
    accepted = Column(Boolean)
    timestamp = Column(DateTime, default=datetime.utcnow)
