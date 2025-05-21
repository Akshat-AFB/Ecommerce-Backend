from repositories.cart_repo import cartRepository
from schemas.cart import CartItem
class CartService:
    @staticmethod
    def add_to_cart(item, user_id: str):
        return cartRepository.add_to_cart(item, user_id)

    @staticmethod
    def get_cart(user_id):
        return cartRepository.view_cart(user_id)


    @staticmethod
    def remove_from_cart(user_id: str, item: CartItem):
        return cartRepository.remove_from_cart(user_id, item)