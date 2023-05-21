from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    access_token: Optional[str]
    uuid: Optional[UUID] = Field(default_factory=uuid4)


class User(UserBase):
    uuid: UUID
    access_token: str

    class Config:
        orm_mode = True
