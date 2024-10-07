from fastapi import FastAPI

from src.back.routers.account.user_router import user_router
from src.back.routers.account.auth_router import auth_router
from src.back.routers.token_router import token_router

app = FastAPI()
app.include_router(token_router)
app.include_router(user_router)
app.include_router(auth_router)
