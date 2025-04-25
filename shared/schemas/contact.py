# shared/schemas/contact.py
from pydantic import BaseModel, EmailStr

class Contact(BaseModel):
    id: int
    name: str
    email: EmailStr
