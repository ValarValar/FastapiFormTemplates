from functools import lru_cache

from dotenv import find_dotenv
from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api"
    APP_NAME: str = "Forms API"
    MONGODB_DOCKER_URL: str
    MONGODB_DATABASE: str
    MONGODB_COLLECTION: str
    MONGODB_LOCAL_URL: str

    class Config:
        env_file = find_dotenv(filename=".env.dev", usecwd=True)


@lru_cache()
def get_settings():
    return Settings()
