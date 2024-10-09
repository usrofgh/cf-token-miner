from pydantic import BaseModel


class TokenCreate(BaseModel):
    site_url: str
    token: str


class TokenRead(BaseModel):
    site_url: str
