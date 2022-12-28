from fastapi import FastAPI

from . import api
from .config import config, Environment
from .database import initialize_database

initialize_database()

app_configs = {}
if config.ENV == Environment.PRODUCTION:
    app_configs["docs_url"] = None

app = FastAPI(**app_configs)

app.include_router(api.router, prefix="/api")
app.router.redirect_slashes = False
