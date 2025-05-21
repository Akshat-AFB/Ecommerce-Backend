from repositories.cart_repo import cartRepository

class CartService:
    @staticmethod
    def add_to_cart(user_id: str, item):
        return cartRepository.add_to_cart(user_id, item)

    @staticmethod
    def get_cart(user_id: str):
        return cartRepository.view_cart(user_id)


    @staticmethod
    def remove_from_cart(user_id, item):
        return cartRepository.remove_from_cart(user_id, item)