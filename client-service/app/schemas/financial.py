from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class FinancialCreate(BaseModel):
    category: str = Field(..., example="Marketing")
    amount: float = Field(..., example=3500.0)
    entry_date: date = Field(..., example="2025-04-10")

class FinancialOut(FinancialCreate):
    id: int

    class Config:
        from_attributes = True
