from fastapi import APIRouter, status, Depends

from src.back.dependencies import get_current_user
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
    dependencies=[Depends(get_current_user)]
)
def get_token(data: TokenRead):
    token =  redis_manager.get(data.site_url)
    if not token:
        return "ABSENT"
    return token


@token_router.post(
    path="/add",
    description="Add CF token for the specific site to Redis",
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(get_current_user)]
)
def add_token(data: TokenCreate):
    redis_manager.add(key=data.site_url, value=data.token)
    return "OK"
