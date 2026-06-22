from fastapi import APIRouter, HTTPException, status
from app.schemas.store import StoreCreate, StoreResponse
from app.repository.store import create_store as db_create_store
from app.repository.store import get_all_stores as db_get_all_stores

router = APIRouter(prefix="/api/v1/store", tags=["store"])

@router.post("/", response_model=StoreResponse, status_code=status.HTTP_201_CREATED)
def create_store(request: StoreCreate)-> StoreResponse:
    db_create_store(request)
    return {
  "name": request.name,
  "city": request.city,
  "area": request.area,
  "address": request.address,
  "id": 0,
  "description": "Store created Successfully"
}

@router.get("/", response_model=list[StoreResponse])
def get_all_stores() -> list[StoreResponse]:
    return db_get_all_stores()