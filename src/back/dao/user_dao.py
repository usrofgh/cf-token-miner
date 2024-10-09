from src.back.dao.base_dao import BaseDAO, ModelType
from src.back.models.user_model import UserModel
from sqlalchemy.orm import Session
from typing import Optional

from src.back.schemas.user_schemas import UserCreateSchema, UserUpdateSchema


class UserDAO(BaseDAO):
    MODEL = UserModel

    @classmethod
    def create_user(cls, db: Session, obj_in: UserCreateSchema):
        cls._create(db=db, obj_in=obj_in)

    @classmethod
    def read_by_email(cls, db: Session, email: str) -> Optional[MODEL]:
        return cls._read_by(db=db, email=email)

    @classmethod
    def update_user(cls, db: Session, db_obj: UserModel, obj_in: UserUpdateSchema) -> None:
        cls._update(db=db, db_obj=db_obj, obj_in=obj_in)

    @classmethod
    def delete_user(cls, db: Session, db_obj: ModelType) -> None:
        cls._delete(db=db, db_obj=db_obj)
