from fastapi import FastAPI
from routes import userRoutes

app = FastAPI(title="E-Commerce Backend", version="1.0")


app.include_router(userRoutes.router, prefix="/users", tags=["Users"])
# app.include_router(product_routes.router, prefix="/products", tags=["Products"])
# app.include_router(cart_routes.router, prefix="/cart", tags=["Cart"])
# app.include_router(order_routes.router, prefix="/orders", tags=["Orders"])