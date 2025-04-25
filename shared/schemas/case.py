# shared/schemas/case.py
from pydantic import BaseModel
from typing import Literal

class Case(BaseModel):
    id: str
    title: str
    status: Literal["open", "closed"]
