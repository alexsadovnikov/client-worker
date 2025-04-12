from pydantic import BaseModel

class Interaction(BaseModel):
    id: int
    type: str
    description: str
