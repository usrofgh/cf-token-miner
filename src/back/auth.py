import datetime
import jwt
from typing import Optional

from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from src.back.dao.user_dao import UserDAO
from src.back.models.user_model import UserModel
from src.config import config

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def create_access_token(data: dict, expires_delta: datetime.timedelta | None = None) -> str:
    to_encode = data.copy()
    to_encode.update({"exp": expires_delta})
    encoded_jwt = jwt.encode(
        claims=to_encode,
        key=config.SECRET_KEY,
        algorithm=config.JWT_ALGORITHM
    )
    return encoded_jwt

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def authenticate_user(db: Session, email: str, password: str) -> Optional[UserModel]:
    user = UserDAO.read_by_email(db=db, email=email)
    if user and verify_password(password, user.password):
        return user
