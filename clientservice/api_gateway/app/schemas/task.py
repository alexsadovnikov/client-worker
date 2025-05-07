from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class TaskCreate(BaseModel):
    title: str = Field(..., example="Fix bugs")
    description: Optional[str] = Field(None, example="Fix bugs in auth module")
    status: str = Field(..., example="in_progress")
    due_date: Optional[datetime] = Field(None, example="2025-04-30T00:00:00")
    priority: Optional[int] = Field(None, example=1)

class TaskOut(TaskCreate):
    id: int

    class Config:
        from_attributes = True
class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, example="Fix bugs")
    description: Optional[str] = Field(None, example="Fix bugs in auth module")
    status: Optional[str] = Field(None, example="completed")
    due_date: Optional[datetime] = Field(None, example="2025-05-30T00:00:00")
    priority: Optional[int] = Field(None, example=2)
