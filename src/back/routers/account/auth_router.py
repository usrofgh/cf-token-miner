from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from src.back.dependencies import get_db
from src.back.schemas.auth import AuthTokenRead
from src.back.schemas.user_schemas import UserLoginSchema
from src.back.services.auth_service import AuthService

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
    return AuthService.login_for_access_token(db=db, user=user)
