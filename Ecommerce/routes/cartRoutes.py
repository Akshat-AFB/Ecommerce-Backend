from fastapi import APIRouter, HTTPException, status, Depends
from services.cartService import CartService
from authentication.auth_dependency import get_current_user
from schemas.cart import CartItem, AddToCartRequest, RemoveFromCartRequest
router = APIRouter()

@router.post("/add", status_code=status.HTTP_201_CREATED)
async def add_to_cart(item: CartItem, user_id: str):
    try:
        return CartService.add_to_cart( item, user_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
@router.get("/{user_id}", status_code=status.HTTP_200_OK)

async def get_cart(user_id: str):
    try:
        return CartService.get_cart(user_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    

@router.put("/remove", status_code=status.HTTP_200_OK)

async def remove_from_cart(user_id: str, item: CartItem):
    try:
        return CartService.remove_from_cart(user_id, item)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    

