from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn


app = FastAPI(
    title="WTE",
)

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
