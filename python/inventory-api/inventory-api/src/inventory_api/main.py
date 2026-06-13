from fastapi import FastAPI,Header
from pydantic import BaseModel

from inventory_api.routers.v1.products import router
from inventory_api.routers.v1.products import router as product_router

app = FastAPI(title="Inventory API")

# @app.get("/health")
# def health_check():
#     return {"status": "ok"}
APP_V1 = "/api/v1"
app.include_router(product_router, prefix=APP_V1)

#@app.get("/items")
#def list_items():
#    return [{"id": 1, "name": "Widget", "quantity": 10}]


# @app.get("/users/{user_id}")
# async def get_user(user_id: int):
#     """This api will return user information
#     """
#     print(f"fetching informaton for user with id {user_id}")
#     return {
#         "id": user_id,
#         "name": "John Doe",
#         "email": "john.doe@example.com"
#     }

# #@app.post("/products")
# #async def create_product(product: Product):
# #   return product


# @app.post("/users")
# async def create_user(user: User):
#     return user

# @app.post("/suppliers")
# async def create_supplier(supplier: Supplier):
#     return supplier


# @app.get("/products")
# async def get_products(category: str, limit: int = 10):
#     return {
#         "category": category,
#         "limit": limit,
#     }
