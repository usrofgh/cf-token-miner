from pydantic import BaseModel

class AuthTokenRead(BaseModel):
    access_token: str
    token_type: str
