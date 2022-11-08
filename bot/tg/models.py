from __future__ import annotations

from pydantic import BaseModel, Field


class MessageFrom(BaseModel):
    id: int
    first_name: str
    last_name: str or None = None
    username: str or None = None


class Chat(BaseModel):
    id: int
    type: str
    first_name: str or None = None
    last_name: str or None = None
    username: str or None = None
    title: str or None = None


class Message(BaseModel):
    message_id: int
    from_: MessageFrom = Field(..., alias="from")
    chat: Chat
    text: str or None = None

    class Config:
        allow_population_by_field_name = True


class UpdateObj(BaseModel):
    update_id: int
    message: Message


class GetUpdateResponse(BaseModel):
    ok: bool
    result: list[UpdateObj] = []


class SendMessageResponse(BaseModel):
    ok: bool
    result: Message
