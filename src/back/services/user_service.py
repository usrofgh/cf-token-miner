from sqlalchemy.exc import IntegrityError

from src.back.auth import get_password_hash
from src.back.dao.user_dao import UserDAO
from src.back.exceptions.user_exception import UserExistException, UserNotFoundException
from src.back.models.user_model import UserModel
from src.back.schemas.user_schemas import UserCreateSchema, UserUpdateSchema
from sqlalchemy.orm import Session


class UserService:
    @staticmethod
    def create_user(db: Session, user: UserCreateSchema) -> None:
        user.password = get_password_hash(user.password)

        try:
            UserDAO.create_user(db=db, obj_in=user)
        except IntegrityError as e:
            db.rollback()
            if "unique constraint" in str(e):
                raise UserExistException

    @staticmethod
    def read_user_by_id(db: Session, id: int) -> UserModel:
        user = UserDAO.read_by_id(db=db, id=id)
        if not user:
            raise UserNotFoundException
        return user

    @staticmethod
    def read_user_by_email(db: Session, email: str) -> UserModel:
        user = UserDAO.read_by_email(db=db, email=email)
        if not user:
            raise UserNotFoundException
        return user

    @staticmethod
    def update_user(db: Session, user: UserUpdateSchema) -> None:
        db_user = UserDAO.read_by_id(db=db, id=user.id)
        if not db_user:
            raise UserNotFoundException
        UserDAO.update_user(db=db, db_obj=db_user, obj_in=user)

    @staticmethod
    def delete_user(db: Session, id: int) -> None:
        user = UserDAO.read_by_id(db=db, id=id)
        if not user:
            raise UserNotFoundException

        UserDAO.delete_user(db=db, db_obj=user)
