from pydantic import BaseModel, Field

class LoginSchema(BaseModel):
    username: str = Field(..., example="admin")
    password: str = Field(..., example="secret")