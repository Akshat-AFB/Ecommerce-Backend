from fastapi import APIRouter, HTTPException, status
from services.productService import ProductService
from schemas.product import ProductCreate


router = APIRouter()

@router.get("/")
async def list_products(offset: int = 0, limit: int = 10):
    return ProductService.list_products(offset, limit)

@router.get("/{product_id}")
async def get_product(product_id: int):
    product = ProductService.get_product(product_id)
    if not product:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product

@router.post("/")
async def create_product(product: ProductCreate):
    return ProductService.create_product(product)