import os
from functools import lru_cache
from pydantic_settings import BaseSettings
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings(BaseSettings):
    # App
    APP_NAME: str = os.environ.get("APP_NAME", "FastAPI")
    DEBUG: bool = bool(os.environ.get("DEBUG", False))

    # Sql Database Config
    DATABASE_URI: str = os.environ.get(
        "DATABASE_URI", "postgres://user:admin@localhost:5432/food-factory"
    )

    # App Secret Key
    SECRET_KEY: str = os.environ.get(
        "SECRET_KEY", "8deadce9449770680910741063cd0a3fe0acb62a8978661f421bbc"
    )


@lru_cache()
def get_settings() -> Settings:
    return Settings()
