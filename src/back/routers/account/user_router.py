from fastapi import APIRouter, status, Depends
from src.back.dependencies import get_db, get_current_admin_user, get_current_user
from src.back.schemas.user_schemas import UserReadSchema, UserCreateSchema, UserUpdateSchema, UserByEmail
from sqlalchemy.orm import Session

from src.back.services.user_service import UserService

user_router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@user_router.post(
    path="/",
    status_code=status.HTTP_201_CREATED
)
def create_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    UserService.create_user(db=db, user=user)


@user_router.get(
    path="/{id}",
    response_model=UserReadSchema,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_current_admin_user)]
)
def read_user(id: int, db: Session = Depends(get_db)):
    return UserService.read_user_by_id(db=db, id=id)

@user_router.post(
    path="",
    response_model=UserReadSchema,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_current_admin_user)]
)
def read_user_by_email(user: UserByEmail, db: Session = Depends(get_db)):
    return UserService.read_user_by_email(db=db, email=user.email)

@user_router.delete(
    path="/{id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_user(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    UserService.delete_user(db=db, id=current_user.id)
