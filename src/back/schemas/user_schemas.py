from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserCreateSchema(BaseModel):
    email: EmailStr
    password: str

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
