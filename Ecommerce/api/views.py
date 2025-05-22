from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .models import CartItem, Order, OrderItem, Cart
from .serializers import CartItemSerializer, OrderSerializer, CartSerializer
from datetime import datetime

User = get_user_model()

class SecretView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": f"Hello {request.user.username}, you're authenticated!"})

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims if needed
        token['username'] = user.username
        token['role'] = user.role  # Assuming you extended AbstractUser with 'role'
        return token

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        if User.objects.filter(username=data['username']).exists():
            return Response({"error": "Username already exists"}, status=400)
        if(data['role'] == 'public'):
            user = User.objects.create_user(
                username=data['username'],
                email=data.get('email', ''),
                password=data['password'],
                role=data.get('role', 'public')
            )
            user.save()
            return Response({"message": "Public User created"}, status=201)
        else:
            user = User.objects.create_superuser(
                username=data['username'],
                email=data.get('email', ''),
                password=data['password'],
                role=data.get('role', 'admin')
            )
            user.save()
            return Response({"message": "Admin User created"}, status=201)
        return Response({"message": "Error in creating user. Try Again !"}, status=500)
    
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]


# Admin: Create, Update, Delete Products

class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser]

class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser]

class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser]


class CartListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user

        try:
            cart = Cart.objects.get(user=user)
        except Cart.DoesNotExist:
            return Response({"items": [], "cart_total": 0}, status=status.HTTP_200_OK)

        cart_items = cart.cart_items.all()
        serializer = CartItemSerializer(cart_items, many=True)
        total = sum(item.quantity * item.product.price for item in cart_items)

        return Response({
            "items": serializer.data,
            "cart_total": total
        }, status=status.HTTP_200_OK)

# Add or update a cart item
class AddToCartView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = request.user
        product_id = request.data.get('product')
        quantity = int(request.data.get('quantity', 1))

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)

        # Get or create cart for user
        cart, _ = Cart.objects.get_or_create(user=user)

        # Get or create cart item
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={'quantity': quantity}
        )

        if not created:
            if cart_item.quantity + quantity > product.stock:
                return Response({'error': 'Exceeds available stock.'}, status=400)
            cart_item.quantity += quantity
            cart_item.save()

        return Response({'message': 'Product added to cart.'}, status=status.HTTP_200_OK)


class ChangeCartItemQuantityView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, product_id):
        action = request.data.get("action")  # should be 'increment' or 'decrement'

        if action not in ['increment', 'decrement']:
            return Response({"detail": "Invalid action. Must be 'increment' or 'decrement'."},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"detail": "Product not found."}, status=status.HTTP_404_NOT_FOUND)

        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        if action == 'increment':
            if cart_item.quantity >= product.stock:
                return Response({"detail": "Cannot exceed available stock."}, status=status.HTTP_400_BAD_REQUEST)
            cart_item.quantity += 1
        elif action == 'decrement':
            if cart_item.quantity <= 1:
                return Response({"detail": "Quantity cannot be less than 1."}, status=status.HTTP_400_BAD_REQUEST)
            cart_item.quantity -= 1

        cart_item.save()
        return Response({"detail": f"Quantity {action}ed successfully.", "quantity": cart_item.quantity}, status=200)

# Remove item from cart
class RemoveFromCartView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, product_id):
        try:
            cart = Cart.objects.get(user=request.user)
        except Cart.DoesNotExist:
            return Response({"detail": "Cart not found."}, status=status.HTTP_404_NOT_FOUND)

        try:
            cart_item = CartItem.objects.get(cart=cart, product_id=product_id)
            cart_item.delete()
            return Response({"detail": "Item removed from cart."}, status=status.HTTP_200_OK)
        except CartItem.DoesNotExist:
            return Response({"detail": "Item not found in cart."}, status=status.HTTP_404_NOT_FOUND)

    
class PlaceOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user

        try:
            cart = Cart.objects.get(user=user)
        except Cart.DoesNotExist:
            return Response({"detail": "Cart is empty."}, status=status.HTTP_400_BAD_REQUEST)

        cart_items = cart.cart_items.select_related('product')

        if not cart_items.exists():
            return Response({"detail": "Cart has no items."}, status=status.HTTP_400_BAD_REQUEST)

        orders = []

        for item in cart_items:
            product = item.product
            if item.quantity > product.stock:
                return Response({
                    "detail": f"Insufficient stock for {product.name}."
                }, status=status.HTTP_400_BAD_REQUEST)

        # All validations passed, now create orders and deduct stock
        for item in cart_items:
            product = item.product
            product.stock -= item.quantity
            product.save()

            order = Order.objects.create(
                user=user,
                product=product,
                quantity=item.quantity,
                order_date=datetime.now(),
                order_status="placed"
            )
            orders.append(order)

        # Clear the cart
        cart_items.delete()

        return Response({"detail": "Order placed successfully.", "orders": [order.id for order in orders]}, status=201)

class CancelOrderView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, order_id):
        try:
            order = Order.objects.get(id=order_id, user=request.user)
        except Order.DoesNotExist:
            return Response({"detail": "Order not found."}, status=status.HTTP_404_NOT_FOUND)

        if order.order_status == 'cancelled':
            return Response({"detail": "Order is already cancelled."}, status=status.HTTP_400_BAD_REQUEST)

        if order.order_status in ['shipped', 'delivered']:
            return Response({"detail": "Cannot cancel shipped or delivered orders."}, status=status.HTTP_400_BAD_REQUEST)

        order.order_status = 'cancelled'
        order.save()
        return Response({"detail": "Order cancelled successfully."}, status=status.HTTP_200_OK)


# View Past Orders
class OrderListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        limit = int(request.query_params.get('limit', 10))
        offset = int(request.query_params.get('offset', 0))

        orders = Order.objects.filter(user=request.user).order_by('-order_date')
        paginated_orders = orders[offset:offset+limit]

        serializer = OrderSerializer(paginated_orders, many=True)
        return Response({
            "total": orders.count(),
            "limit": limit,
            "offset": offset,
            "orders": serializer.data
        })