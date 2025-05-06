from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr = Field(..., example="user@example.com")
    name: str = Field(..., example="John Doe")
    role: str = Field(..., example="admin")

class UserOut(UserCreate):
    id: int

    class Config:
        from_attributes = True
class UserUpdate(BaseModel):
    email: Optional[str] = Field(None, example="user@example.com")
    full_name: Optional[str] = Field(None, example="John Doe")
    role: Optional[str] = Field(None, example="manager")