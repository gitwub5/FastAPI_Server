from fastapi import APIRouter
from app.api.routes import example_router
#from app.core.config import settings

router = APIRouter()

#라우터 생길 시 추가
router.include_router(example_router.router, prefix="/example", tags=["example"])