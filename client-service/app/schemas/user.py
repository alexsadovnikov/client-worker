from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    email: EmailStr = Field(..., example="user@example.com")
    name: str = Field(..., example="John Doe")
    role: str = Field(..., example="admin")

class UserOut(UserCreate):
    id: int

    class Config:
        from_attributes = True
