from fastapi import APIRouter
from app.api.routes import example_router
from app.api.routes import router

router = APIRouter()

router.include_router(router.router)