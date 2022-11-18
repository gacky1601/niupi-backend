from fastapi import APIRouter
from . import user, auth

api_router = APIRouter()

api_router.include_router(user.router, prefix="/user")
api_router.include_router(auth.router, prefix="/auth")
