from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from src.core.config import settings
from src.routers.v1.item import router as item_router
from src.routers.v1.auth import router as auth_router
from src.routers.v1.asset_router import router as assets_router
from src.routers.v1.service_equipment_router import router as se_router
from src.routers.v1.redress_kit_router import router as rk_router

app = FastAPI(
    title="WTE",
    version="1.0.0",
    debug=settings.DEBUG
)

app.include_router(item_router)
app.include_router(auth_router)
app.include_router(assets_router)
app.include_router(se_router)
app.include_router(rk_router)


# Настройка CORS middleware для разрешения запросов с вашего фронтенда
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Здесь лучше указать разрешенные домены фронтенда
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()}),
    )


@app.get("/")
def home_page():
    return {"message": "WTE!"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=5001)
