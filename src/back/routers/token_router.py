from fastapi import APIRouter, status

from src.back.schemas.cf_token_schemas import TokenRead, TokenCreate
from src.managers.redis_manager import redis_manager

token_router = APIRouter(
    prefix="/token",
    tags=["Cloudflare token"]
)

@token_router.post(
    path="/get",
    description="Get CF token for the specific site from Redis",
    status_code=status.HTTP_200_OK,
    response_model=str
)
def get_token(data: TokenRead):
    return redis_manager.get(data.site_url)

@token_router.post(
    path="/add",
    description="Add CF token for the specific site to Redis",
    status_code=status.HTTP_201_CREATED,
    response_model=str
)
def add_token(data: TokenCreate):
    redis_manager.add(key=data.site_url, value=data.token)
    return "OK"
