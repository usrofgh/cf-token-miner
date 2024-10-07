from fastapi import APIRouter, status, Depends

from src.back.dao.user_dao import UserDAO
from src.back.dependencies import get_db
from src.back.exceptions import EntityNotFoundException
from src.back.schemas.user_schemas import UserReadSchema, UserCreateSchema
from sqlalchemy.orm import Session

user_router = APIRouter(
    prefix="/user",
    tags=["User"]
)


@user_router.post(
    path="/",
    response_model=UserReadSchema,
    status_code=status.HTTP_201_CREATED
)
def create_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    user = UserDAO.create(db=db, obj_in=user)
    return user


@user_router.get(
    path="/{id}",
    response_model=UserReadSchema,
    status_code=status.HTTP_200_OK,
)
def get_user(id: int, db: Session = Depends(get_db)):
    user = UserDAO.read_by_id(db=db, id=id)
    if not user:
        raise EntityNotFoundException
    return user


@user_router.delete(
    path="/{id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_user(id: int, db: Session = Depends(get_db)):
    UserDAO.delete(db=db, id=id)
