from sqlalchemy import Boolean, Enum, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from enum import Enum as enum


class Chat_by(enum):
    USER = 1
    ASSISTANT = 2

# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     is_active = Column(Boolean, default=True)

#     chats = relationship("Chat", back_populates="user")

# class Chat(Base):
#     __tablename__ = "chats"

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     content = Column(String)
#     sent_time = Column(DateTime)
#     chat_by = Column(Integer, nullable=False)

#     user_id = Column(Integer, ForeignKey("users.id"))
#     user = relationship("User", back_populates="chats")
#     assistant_id = Column(Integer, ForeignKey("assistants.id"))
#     assistant = relationship("Assistant", back_populates="chats")

# class Assistant(Base):
#     __tablename__ = "assistants"

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String, unique=True)

#     chats = relationship("Chat", back_populates="assistant")