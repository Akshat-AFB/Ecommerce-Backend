from pydantic import BaseModel


class Product(BaseModel):
    product_id: int
    name: str
    description: str = None
    price: float
    brand: str
    stock_quantity: int
    image_url: str = None