from fastapi import APIRouter
from . import user, store


api_router = APIRouter()

api_router.include_router(user.router, prefix="/user")
api_router.include_router(store.router, prefix="/store")
