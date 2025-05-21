
import json
class OrderRepository:

    orders = []
    curr_id = 0

    @classmethod
    def create_order(cls,order_data):
        order_data["order_data"] = cls.curr_id
        cls.orders.append(order_data)
        cls.curr_id += 1
        return order_data
    
    @classmethod
    def get_user_orders(cls, user_id, offset, limit: int =10):
        user_orders = []
        for order in cls.orders: 
            if order["user_id"] == user_id:
                user_orders.append(order)
        return user_orders[offset: offset + limit]
    
    @classmethod
    def cancel_order(cls, user_id, order_id):
        updated_orders = []
        f = 0
        for order in cls.orders: 
            if order["user_id"] == user_id and order["order_id"] == order_id:
                f = 1 
                if order["status"]!="Pending":
                    raise Exception("Order cannot be cancelled")
                else:
                    continue
            else:
                updated_orders.append(order)
        orders = updated_orders
        if f:
            return {"message":"Order cancelled successfully"}
        else: 
            return {"message" : "Order already Cancelled"}


