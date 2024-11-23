
from fastapi import APIRouter, FastAPI

from src.api.v1.root_handler import router as root_router
from src.api.v1.search_handler import router as search_router

app = FastAPI()

v1_router = APIRouter(prefix="/v1")

v1_router.include_router(search_router)
v1_router.include_router(root_router)

app.include_router(v1_router)