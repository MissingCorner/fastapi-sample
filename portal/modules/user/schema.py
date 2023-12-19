"""schema"""
from pydantic import BaseModel, EmailStr

from portal.modules.postgres.crud import CRUDBase


class UserBase(BaseModel):
    """User"""

    id: str
    fullname: str
    email: EmailStr


class UserCreate(UserBase):
    "CreateDTO"


class User(UserBase):
    "User entity"

    class Config:
        "ORM"
        from_attributes = True


class UserModel(CRUDBase[User, UserCreate, BaseModel]):
    "User model"


users = UserModel(User)
