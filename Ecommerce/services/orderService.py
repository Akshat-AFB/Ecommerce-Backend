from repositories.orderRepositories import OrderRepository
from datetime import datetime

class OrderService:
    @staticmethod
    def create_order(user_id: str, items: list):
        total_price = sum(item.quantity * item.price for item in items)
        order_data = {
            "user_id": user_id,
            "items": items,
            "total_price": total_price,
            "status": "Success",
            "created_at": datetime.now()
        }
        return OrderRepository.create_order(order_data)
    
    @staticmethod   
    def get_user_orders(user_id: str, offset: int = 0, limit: int = 10):
        return OrderRepository.get_user_orders(user_id, offset, limit)
    
    @staticmethod
    def cancel_order(user_id: str, order_id: int):
        return OrderRepository.cancel_order(user_id, order_id)