from pydantic import BaseSettings, PostgresDsn
from enum import Enum


class Environment(Enum):
    PRODUCTION = "production"
    DEVELOPMENT = "development"


class Settings(BaseSettings):
    ENV: Environment = Environment.PRODUCTION

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    POSTGRESS_ADDRESS: PostgresDsn


config = Settings()
