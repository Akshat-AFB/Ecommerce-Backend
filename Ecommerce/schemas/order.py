from pydantic import BaseModel
from datetime import datetime

class OrderItemSchema(BaseModel):
    product_id: int
    quantity: int

class OrderCreate(BaseModel):
    user_id: str
    items: list[OrderItemSchema]

class OrderResponse(BaseModel):
    order_id: int
    user_id: str
    items: list[OrderItemSchema]
    total_price: float
    order_date: datetime
    status: str  # PENDING, SHIPPED, DELIVERED