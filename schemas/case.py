from pydantic import BaseModel
from typing import Optional

class Case(BaseModel):
    id: str
    title: str
    status: Optional[str] = None
