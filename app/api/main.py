# from fastapi import APIRouter
# # from routes import example_router
# from app.api.routes import router

# route = APIRouter()

# route.include_router(router.router)


from fastapi import APIRouter
from app.api.routes.router import router as app_router  # app_router로 이름 변경하여 가져옴

router = APIRouter()

router.include_router(app_router)  # app_router를 api_router에 포함시킴