from pydantic import BaseModel

class Case(BaseModel):
    id: str
    title: str
    status: str
