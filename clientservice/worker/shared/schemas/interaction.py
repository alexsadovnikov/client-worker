from pydantic import BaseModel
from typing import Optional

class Interaction(BaseModel):
    id: str
    type: str
    contact_id: str
    case_id: Optional[str] = None
    message: Optional[str] = None
    timestamp: Optional[str] = None
