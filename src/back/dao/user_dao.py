from src.back.dao.base_dao import BaseDAO
from src.back.models.user_model import UserModel


class UserDAO(BaseDAO):
    MODEL = UserModel
