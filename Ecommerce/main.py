from fastapi import FastAPI
from routes import userRoutes, productRoutes, cartRoutes

app = FastAPI(title="E-Commerce Backend", version="1.0")


app.include_router(userRoutes.router, prefix="/users")
app.include_router(productRoutes.router, prefix="/products")
app.include_router(cartRoutes.router, prefix="/cart")
# app.include_router(order_routes.router, prefix="/orders", tags=["Orders"])