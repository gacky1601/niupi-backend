from fastapi import FastAPI

from . import api
from .database import initialize_db

initialize_db()

app = FastAPI()

app.include_router(api.router, prefix="/api")
