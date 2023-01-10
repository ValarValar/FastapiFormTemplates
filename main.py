from functools import lru_cache

from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from api.endpoints.forms import router as forms_router
from core.config import Settings


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()

app = FastAPI(
    title=settings.APP_NAME,
    docs_url="/api/openapi",
    redoc_url="/api/redoc",
    # Адрес документации в формате OpenAPI
    openapi_url="/api/openapi.json",
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient(settings.MONGODB_URL)
    app.mongodb = app.mongodb_client[settings.MONGODB_DATABASE]


@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()


app.include_router(router=forms_router, prefix="/api/forms")
