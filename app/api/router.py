from fastapi import APIRouter
from . import user

api_router = APIRouter()

api_router.include_router(user.router, prefix="/user")
