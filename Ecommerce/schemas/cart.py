from pydantic import BaseModel

class CartItemSchema(BaseModel):
    product_id: int
    quantity: int

class AddToCartRequest(BaseModel):
    user_id: str
    items: list[CartItemSchema]

class CartResponse(BaseModel):
    user_id: str
    items: list[CartItemSchema]