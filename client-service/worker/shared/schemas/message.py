from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MessageCreate(BaseModel):
    sender: str
    receiver: str
    content: str
    timestamp: Optional[datetime] = None
