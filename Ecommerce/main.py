from fastapi import FastAPI
from routes import userRoutes, productRoutes

app = FastAPI(title="E-Commerce Backend", version="1.0")


app.include_router(userRoutes.router, prefix="/users")
app.include_router(productRoutes.router, prefix="/products")
# app.include_router(cart_routes.router, prefix="/cart", tags=["Cart"])
# app.include_router(order_routes.router, prefix="/orders", tags=["Orders"])