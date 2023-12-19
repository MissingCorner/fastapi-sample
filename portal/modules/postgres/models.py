"""User model"""
from sqlalchemy import Column, String

from .database import Base


class User(Base):
    """model"""

    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    email = Column(String)
    fullname = Column(String)
