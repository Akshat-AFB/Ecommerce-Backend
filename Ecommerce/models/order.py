from pydantic import BaseModel
from datetime import datetime
from product import Product

class OrderItem(BaseModel):
    product_id: int
    quantity: int
    Product.price

class Order(BaseModel):
    order_id: int
    user_id: str
    items: list[OrderItem]
    total_price: float
    order_date: datetime
    status: str  # e.g., "Pending", "Shipped", "Delivered"