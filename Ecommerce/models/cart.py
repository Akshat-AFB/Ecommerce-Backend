from pydantic import BaseModel

class CartItem(BaseModel):
    product_id: int
    quantity: int

class Cart(BaseModel):
    user_id: str
    items: list[CartItem]
    total_price: float = 0.0  