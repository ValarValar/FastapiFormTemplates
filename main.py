from fastapi import FastAPI

from api.endpoints.forms import router as forms_router
from core.config import get_settings
from utils.db_service import get_mongodb_service, MongoDbService

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
    app.db_service: MongoDbService = get_mongodb_service()


@app.on_event("shutdown")
async def shutdown_db_client():
    app.db_service.mongodb_client.close()


app.include_router(router=forms_router, prefix="/api/forms")
