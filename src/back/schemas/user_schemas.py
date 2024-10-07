from datetime import datetime

from pydantic import BaseModel, EmailStr, Field


class UserCreateSchema(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=100)

class UserReadSchema(BaseModel):
    id: int
    email: EmailStr
    is_superuser: bool
    is_verified: bool
    registered_at: datetime

class UserInDB(UserReadSchema):
    password: str

class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str
