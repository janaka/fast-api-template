"""Root endpoint '/' handler and '/hello' route handler. Unauthenticated endpoints.
These are useful for basic testing that the application is working.
"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
@router.get("/hello")
def get_root():
    return {"Hello": "World"}
