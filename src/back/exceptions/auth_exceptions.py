from fastapi import status
from src.back.exceptions.base_exception import BException


class CredsException(BException):
    STATUS_CODE = status.HTTP_401_UNAUTHORIZED
    DETAIL = "Could not validate credentials"


class ForbiddenException(BException):
    STATUS_CODE = status.HTTP_403_FORBIDDEN
    DETAIL = "Not enough rules"
