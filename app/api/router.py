from fastapi import APIRouter
from . import user, users

api_router = APIRouter()

api_router.include_router(user.router, prefix="/user")

api_router.include_router(users.router, prefix="/users")