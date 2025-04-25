# shared/schemas/message.py
from pydantic import BaseModel, Field

class MessageCreate(BaseModel):
    sender_id: str = Field(..., description="ID отправителя")
    recipient_id: str = Field(..., description="ID получателя")
    content: str = Field(..., description="Текст сообщения")
