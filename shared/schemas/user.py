from pydantic import BaseModel, EmailStr, Field

class UserLogin(BaseModel):
    email: EmailStr = Field(..., example="admin@example.com")
    password: str = Field(..., example="securepassword")