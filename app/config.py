from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    POSTGRESS_ADDRESS: PostgresDsn


config = Settings()
