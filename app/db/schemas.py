from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    """ User schema. """
    name: Optional[str] = None
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True


class UserUpdate(UserBase):
    id: Optional[int] = None
    email: Optional[str] = None
    password: Optional[str] = None

