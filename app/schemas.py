# app/schemas.py
from pydantic import BaseModel

class CaseSearchRequest(BaseModel):
    state: str
    commission: str
    search_value: str
