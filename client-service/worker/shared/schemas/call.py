from pydantic import BaseModel
from typing import Optional

class Call(BaseModel):
    id: str
    contact_id: str
    agent_id: str
    datetime: str
    duration: Optional[int] = None
    direction: Optional[str] = None
