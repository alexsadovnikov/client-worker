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
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class FinancialRecordCreate(BaseModel):
    category: str = Field(..., example="revenue")
    amount: float = Field(..., example=10000.0)
    date: datetime = Field(..., example="2025-04-01T00:00:00")
    description: Optional[str] = Field(None, example="Client payment for Q1")

class FinancialRecordUpdate(BaseModel):
    category: Optional[str] = Field(None, example="expense")
    amount: Optional[float] = Field(None, example=750.0)
    date: Optional[datetime] = Field(None, example="2025-04-15T00:00:00")
    description: Optional[str] = Field(None, example="Correction")