from pydantic import BaseModel

class Agent(BaseModel):
    id: int
    name: str
    role: str
