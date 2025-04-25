# shared/schemas/call.py
from pydantic import BaseModel

class Call(BaseModel):
    id: str
    agent_id: str
    contact_id: str
