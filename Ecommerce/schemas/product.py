from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    description: str = None
    price: float
    brand: str
    stock_quantity: int
    image_url: str = None

class ProductResponse(BaseModel):
    id: int
    name: str
    description: str = None
    price: float
    brand: str
    stock_quantity: int
    image_url: str = None