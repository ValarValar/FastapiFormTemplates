from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api"
    APP_NAME: str = "Forms API"
    MONGODB_URL: str
    MONGODB_DATABASE: str
    MONGODB_COLLECTION: str

    class Config:
        env_file = ".env.dev"
