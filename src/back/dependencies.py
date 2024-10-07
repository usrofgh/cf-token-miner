import jwt

from typing import Annotated
from fastapi import Depends

from src.back.auth import oauth2_scheme
from src.back.dao.user_dao import UserDAO
from src.back.database import SessionLocal
from sqlalchemy.orm import Session
from src.back.exceptions import IncorrectCredsException, CredsException, ForbiddenException
from src.back.models.user_model import UserModel
from src.logger import config
from jwt.exceptions import InvalidTokenError


def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Session = Depends(get_db)
) -> UserModel:
    try:
        payload = jwt.decode(jwt=token, key=config.SECRET_KEY, algorithms=[config.JWT_ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise CredsException

    except InvalidTokenError:
        raise IncorrectCredsException

    user = UserDAO.read_by_email(db=db, email=email)
    if user is None:
        raise IncorrectCredsException
    return user

def get_current_admin_user(
    current_user: Annotated[UserModel, Depends(get_current_user)],
) -> UserModel:
    if current_user.is_superuser is False:
        raise ForbiddenException
    return current_user
