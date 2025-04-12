from pydantic import BaseModel
from typing import Optional

class Agent(BaseModel):
    id: str
    name: str
    status: Optional[str] = None
