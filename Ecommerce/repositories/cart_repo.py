from schemas.cart import CartItem

class cartRepository:

    carts = {}
    
    @classmethod
    def add_to_cart(cls, item: CartItem, user_id: str):
        if user_id not in cls.carts:
            cls.carts[user_id] = {}
        if item.product_id not in cls.carts[user_id]:
            cls.carts[user_id][item.product_id] = item
        else:
            cls.carts[user_id][item.product_id].quantity += 1
        return {"user_id": user_id, "items": cls.carts[user_id]}

    @classmethod
    def view_cart(cls, user_id: str):
        if user_id not in cls.carts:
            raise Exception("Cart is empty")
        return {"user_id": user_id, "items": cls.carts[user_id]}
    
    @classmethod
    def remove_from_cart(cls, user_id: str, item: CartItem):
        if user_id not in cls.carts:
            raise Exception("Cart is empty")
        if item.product_id not in cls.carts[user_id]:
            raise Exception("Item not in cart")
        else:
            if cls.carts[user_id][item.product_id].quantity == 1:
                del cls.carts[user_id][item.product_id]
            else:
                cls.carts[user_id][item.product_id].quantity -= 1
        return {"user_id": user_id, "items": cls.carts[user_id]}

    