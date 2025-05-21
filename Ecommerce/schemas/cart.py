from pydantic import BaseModel

class CartItem(BaseModel):
    product_id: int
    quantity: int

class AddToCartRequest(BaseModel):
    user_id: str
    item: CartItem

class RemoveFromCartRequest(BaseModel):
    user_id: str
    item: CartItem

class CartResponse(BaseModel):
    user_id: str
    items: list[CartItem]