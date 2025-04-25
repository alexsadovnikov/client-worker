from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class TimesheetCreate(BaseModel):
    user_id: int = Field(..., example=1)
    project_id: int = Field(..., example=2)
    date: Optional[datetime] = Field(default_factory=datetime.utcnow)
    hours: float = Field(..., example=8.0)
    description: Optional[str] = Field(None, example="Worked on frontend module")

class TimesheetOut(TimesheetCreate):
    id: int

    class Config:
        from_attributes = True
