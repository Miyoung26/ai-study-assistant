from datetime import date, datetime
from pydantic import BaseModel, Field

class DataCreate(BaseModel):
    date: date
    value: float = Field(ge=0, le=1440)
    memo: str = Field(default="", max_length=200)

class DataUpdate(DataCreate):
    pass

class Message(BaseModel):
    role: str = Field(pattern="^(user|assistant)$")
    content: str = Field(min_length=1, max_length=4000)

class ConversationCreate(BaseModel):
    title: str = Field(default="새 대화", max_length=100)
    messages: list[Message]

class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=2000)
    conversation_id: str | None = None
    messages: list[Message] = []
