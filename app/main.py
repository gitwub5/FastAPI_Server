from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.main import router as api_router

app = FastAPI(default_response_headers={"Content-Type": "application/json; charset=utf-8"})
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins={"*"},
    allow_credentials=True,
    allow_methods={"OPTIONS", "GET", "POST", "DELETE", "PUT"},
    allow_headers={"*"},
)

from app.core import models
from app.core.database import engine
models.Base.metadata.create_all(bind=engine)
    



