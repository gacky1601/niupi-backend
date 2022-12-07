from fastapi import FastAPI

from . import api
from .config import config, Environment
from .database import initialize_db

initialize_db()

app_configs = {}
if config.ENV == Environment.PRODUCTION:
    app_configs["docs_url"] = None

app = FastAPI(**app_configs)

app.include_router(api.router, prefix="/api")
