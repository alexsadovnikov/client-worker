from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ProjectCreate(BaseModel):
    name: str = Field(..., example="CRM Integration")
    description: Optional[str] = Field(None, example="CRM integration with mobile app")
    status: str = Field(..., example="active")
    start_date: Optional[datetime] = Field(None, example="2025-04-01T00:00:00")
    end_date: Optional[datetime] = Field(None, example="2025-12-01T00:00:00")
    budget: Optional[float] = Field(None, example=15000.0)

class ProjectOut(ProjectCreate):
    id: int

    class Config:
        from_attributes = True

class ProjectUpdate(BaseModel):
    name: Optional[str] = Field(None, example="CRM Integration")
    description: Optional[str] = Field(None, example="Updated description")
    status: Optional[str] = Field(None, example="completed")
    start_date: Optional[datetime] = Field(None, example="2025-04-01T00:00:00")
    end_date: Optional[datetime] = Field(None, example="2025-12-01T00:00:00")
    budget: Optional[float] = Field(None, example=20000.0)
