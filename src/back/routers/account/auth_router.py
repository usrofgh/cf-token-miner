from datetime import timedelta

from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from src.back.auth import authenticate_user, create_access_token
from src.back.dependencies import get_db
from src.back.exceptions import IncorrectCredsException
from src.back.schemas.auth import AuthTokenRead
from src.back.schemas.user_schemas import UserLoginSchema
from src.logger import config

auth_router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@auth_router.post(
    path="/token",
    status_code=status.HTTP_200_OK,
    response_model=AuthTokenRead

)
def login_for_access_token(user: UserLoginSchema, db: Session = Depends(get_db)):
    user_db = authenticate_user(db=db, email=user.email, password=user.password)
    if not user_db:
        raise IncorrectCredsException

    data = {"sub": user.email}
    expires_delta = timedelta(minutes=config.JWT_TTL_MIN)
    access_token = create_access_token(data=data, expires_delta=expires_delta)
    token = AuthTokenRead(access_token=access_token, token_type="bearer")
    return token
