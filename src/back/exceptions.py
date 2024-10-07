from fastapi import HTTPException, status


class BException(HTTPException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = ""

    def __init__(self) -> None:
        super().__init__(status_code=self.status_code, detail=self.detail)

class EntityNotFoundException(BException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Entity not found"


class IncorrectCredsException(BException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Incorrect credentials"


class CredsException(BException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Could not validate credentials"

class ForbiddenException(BException):
    status_code = status.HTTP_403_FORBIDDEN
    detail = "Not enough rules"
