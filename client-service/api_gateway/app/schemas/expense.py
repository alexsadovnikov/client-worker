from pydantic import BaseModel, Field
from typing import Optional
from datetime import date as dt_date  # ✅ Переименуем тип, чтобы избежать конфликта


class ExpenseCreate(BaseModel):
    project_id: int = Field(..., example=1)
    description: str = Field(..., example="Hosting fees")
    amount: float = Field(..., example=100.0)
    spent_at: dt_date = Field(..., example="2025-04-20")  # ✅ новое имя поля


class ExpenseOut(BaseModel):
    id: int
    project_id: int
    description: str
    amount: float
    spent_at: dt_date  # ✅ должно соответствовать схеме выше

    class Config:
        orm_mode = True
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ExpenseCreate(BaseModel):
    amount: float = Field(..., example=150.0)
    category: str = Field(..., example="travel")
    date: datetime = Field(..., example="2025-04-30T00:00:00")
    description: Optional[str] = Field(None, example="Taxi to airport")

class ExpenseUpdate(BaseModel):
    amount: Optional[float] = Field(None, example=200.0)
    category: Optional[str] = Field(None, example="food")
    date: Optional[datetime] = Field(None, example="2025-05-01T00:00:00")
    description: Optional[str] = Field(None, example="Dinner with client")

class ExpenseOut(ExpenseCreate):
    id: int

    class Config:
        from_attributes = True