# shared/schemas/interaction.py
from pydantic import BaseModel
from typing import Optional

class Interaction(BaseModel):
    id: str
    call_id: str
    notes: Optional[str] = None
    rating: Optional[int] = None
