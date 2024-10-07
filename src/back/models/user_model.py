from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.sql import func

from src.back.database import BaseModel


class UserModel(BaseModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, unique=False, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)
    registered_at = Column(DateTime, server_default=func.now())
