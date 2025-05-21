from pydantic import BaseModel
from datetime import datetime

class OrderItem(BaseModel):
    product_id: int
    quantity: int
    price: int

class OrderCreateRequest(BaseModel):
    user_id: str
    items: list[OrderItem]

class OrderResponse(BaseModel):
    order_id: int
    user_id: str
    items: list[OrderItem]
    total_price: float
    order_date: datetime
    status: str  # PENDING, SHIPPED, DELIVERED