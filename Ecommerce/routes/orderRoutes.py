from fastapi import APIRouter, HTTPException, status
from schemas.order import OrderCreateRequest
from services.orderService import OrderService

router = APIRouter()

@router.post("/createOrder", status_code=status.HTTP_201_CREATED)
async def create_order(request: OrderCreateRequest):
    return OrderService.create_order(request.user_id, request.items)

@router.get("/{user_id}", status_code=status.HTTP_200_OK)
async def get_user_orders(user_id: str, offset: int = 0, limit: int = 10):
    return OrderService.get_user_orders(user_id, offset, limit)

@router.put("/{user_id}/{order_id}", status_code = status.HTTP_200_OK)
async def cancel_order(user_id: str, order_id: int):
    return OrderService.cancel_order(user_id, order_id)