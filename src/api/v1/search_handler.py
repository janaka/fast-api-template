"""Example endpoint handler for a post. Unless the logic is really simple then implement in a module and call here.
NOTE: this should be an authenticated endpoint. Use a decorator to enforce authentication.
"""
from typing import List

from fastapi import APIRouter, HTTPException

from src.api.utils.pydantic.camel_base_model import CamelBaseModel


router = APIRouter()


class SearchRequest(CamelBaseModel):
    query: str
    collection_name: str


class SearchResponse(CamelBaseModel):
    query: str
    collection_name: str
    results: List[str]


@router.post("/search")
def search_embeddings(request: SearchRequest) -> SearchResponse:
    """Receives an embedding and returns the top-1 retrieved document"""
    if not request.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty")
    try:

        # Use the reranker in your search query instead
        results = ["some reaulsts"]

        return SearchResponse(query=request.query, collection_name=request.collection_name, results=results)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Search failed: {str(e)}")