from datetime import timedelta

from src.back.auth import create_access_token, authenticate_user
from src.back.exceptions.user_exception import IncorrectCredsException
from src.back.schemas.auth import AuthTokenRead
from src.back.schemas.user_schemas import UserLoginSchema
from sqlalchemy.orm import Session

from src.config import config


class AuthService:
    @staticmethod
    def login_for_access_token(db: Session, user: UserLoginSchema) -> AuthTokenRead:
        user_db = authenticate_user(db=db, email=user.email, password=user.password)
        if not user_db:
            raise IncorrectCredsException

        data = {"sub": user.email}
        expires_delta = timedelta(minutes=config.JWT_TTL_MIN)
        access_token = create_access_token(data=data, expires_delta=expires_delta)
        token = AuthTokenRead(access_token=access_token, token_type="bearer")
        return token
