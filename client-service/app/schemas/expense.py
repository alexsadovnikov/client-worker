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
