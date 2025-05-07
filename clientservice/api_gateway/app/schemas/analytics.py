from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class AnalyticsCreate(BaseModel):
    report_type: str = Field(..., example="monthly")
    generated_at: datetime = Field(..., example="2025-04-01T00:00:00")
    notes: Optional[str] = Field(None, example="Includes Q1 overview")

class AnalyticsOut(AnalyticsCreate):
    id: int

    class Config:
        from_attributes = True
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class AnalyticsReportCreate(BaseModel):
    report_type: str = Field(..., example="monthly_summary")
    start_date: datetime = Field(..., example="2025-04-01T00:00:00")
    end_date: datetime = Field(..., example="2025-04-30T00:00:00")
    filters: Optional[dict] = Field(None, example={"project_id": 123})