from app.models.store import Store
from app.schemas.store import StoreRequest, StoreResponse
from app.db.base import SessionLocal
from sqlalchemy import select

session = SessionLocal()

def create_store(request: StoreRequest) -> StoreResponse:
    store = Store(
        name=request.name,
        address=request.address,
        city=request.city,
        area=request.area
    )
    session.add(store)
    session.commit()
    session.refresh(store)
    return StoreResponse(
        id=store.id,
        name=store.name,
        address=store.address,
        city=store.city,
        area=store.area
    )
def get_all_stores() -> list[StoreResponse]:
    statement = select(Store)

    stores = session.execute(statement).scalars().all()
    response = []
    for store in stores:
        response.append(
            StoreResponse(
                id=store.id,
                name=store.name,
                address=store.address,
                city=store.city,
                area=store.area
            )
        )
    return response