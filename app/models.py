# app/models.py
from pydantic import BaseModel
from typing import List, Optional

class State(BaseModel):
    id: str
    name: str

class Commission(BaseModel):
    id: str
    name: str
    type: str  # DISTRICT / STATE

class Case(BaseModel):
    case_number: str
    case_stage: str
    filing_date: str
    complainant: str
    complainant_advocate: str
    respondent: str
    respondent_advocate: str
    document_link: str

class CaseSearchRequest(BaseModel):
    state: str
    commission: str
    search_value: str
