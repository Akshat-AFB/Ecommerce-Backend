from rest_framework import serializers
from .models import User, Product, CartItem, Order
from .models import CartItem, Cart, OrderItem, Order

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'



class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_total = serializers.SerializerMethodField()
    class Meta:
        model = CartItem
        fields = ['id', 'product_id', 'product_name', 'quantity', 'product_total']
    
    def get_product_total(self, obj):
        return round(obj.quantity * obj.product.price, 2)

class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True, read_only=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'user', 'cart_items', 'total']
        read_only_fields = ['user']


    def get_total(self, obj):
        return round(sum(item.quantity * item.product.price for item in obj.cart_items.all()), 2)

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')
    class Meta:
        model = OrderItem
        fields = ['product_name', 'quantity', 'price_at_order_time']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'order_status', 'order_date', 'items']


    # def get_items(self, obj):
    #     order_items = OrderItem.objects.filter(order=obj)
    #     return OrderItemSerializer(order_items, many=True).data