from fastapi import status
from src.back.exceptions.base_exception import BException


class IncorrectCredsException(BException):
    STATUS_CODE = status.HTTP_401_UNAUTHORIZED
    DETAIL = "Incorrect credentials"


class UserExistException(BException):
    STATUS_CODE = status.HTTP_409_CONFLICT
    DETAIL = "User with such email already exists"


class UserNotFoundException(BException):
    STATUS_CODE = status.HTTP_404_NOT_FOUND
    DETAIL = "User not found"
