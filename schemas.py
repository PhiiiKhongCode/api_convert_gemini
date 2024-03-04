from pydantic import BaseModel, Field
from typing import Union
from datetime import datetime


# chat pydantic model
class Prompt(BaseModel):
    prompt: Union[str | None] = Field(default=None, description="The prompt to request the model for it send back answer!!!")

class PromptCreate(Prompt):
    sent_time: datetime = datetime.now()
    chat_by: int

class Chat(PromptCreate):
    id: int
    user_id: int
    assistant_id: int
    class Config:
        from_attributes = True
        
# user pydantic model
class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserCreate):
    id: int
    is_active: bool
    chats: list[Chat] = []

    class Config:
        from_attributes = True

# assistant pydantic model
class AssistantBase(BaseModel):
    name: str = 'Gemini-pro'

class AssistantCreate(AssistantBase):
    pass

class Assistant(AssistantCreate):
    id: int
    chats: list[Chat] = []

    class Config:
        from_attributes = True

