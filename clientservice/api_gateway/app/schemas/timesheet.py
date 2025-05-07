from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

# ✅ Создание записи учёта времени
class TimeEntryCreate(BaseModel):
    user_id: int = Field(..., example=1)
    project_id: int = Field(..., example=2)
    date: Optional[datetime] = Field(default_factory=datetime.utcnow)
    hours: float = Field(..., example=8.0)
    description: Optional[str] = Field(None, example="Worked on frontend module")

# ✅ Обновление записи учёта времени
class TimeEntryUpdate(BaseModel):
    hours: Optional[float] = Field(None, example=7.5)
    note: Optional[str] = Field(None, example="Adjusted due to holiday")
    date: Optional[datetime] = Field(None, example="2025-05-01T00:00:00")
    project_id: Optional[int] = Field(None, example=1)
    user_id: Optional[int] = Field(None, example=42)
    description: Optional[str] = Field(None, example="Retrospective update")

# ✅ Вывод схемы
class TimeEntrySchema(BaseModel):
    id: int
    user_id: int
    project_id: int
    date: datetime
    hours: float
    description: Optional[str] = None

    class Config:
        from_attributes = True

class TimesheetCreate(BaseModel):
    user_id: int = Field(..., example=1)
    project_id: int = Field(..., example=2)
    date: Optional[datetime] = Field(default_factory=datetime.utcnow)
    hours: float = Field(..., example=8.0)
    description: Optional[str] = Field(None, example="Task breakdown")

class TimesheetUpdate(BaseModel):
    hours: Optional[float] = Field(None, example=6.5)
    project_id: Optional[int] = Field(None, example=2)
    user_id: Optional[int] = Field(None, example=3)
    description: Optional[str] = Field(None, example="Updated after correction")
