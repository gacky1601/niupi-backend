from fastapi import FastAPI

from . import api
from .database import initialize_db
from .config import config, Environment

initialize_db()

app_configs = {}
if config.ENV == Environment.PRODUCTION:
    app_configs["docs_url"] = None

app = FastAPI(**app_configs)

app.include_router(api.router, prefix="/api")
