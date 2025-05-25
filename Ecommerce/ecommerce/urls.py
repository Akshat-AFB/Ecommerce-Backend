"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views import CustomTokenObtainPairView
from api.views import RegisterView, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, PlaceOrderView, OrderListView
from api.views import CartListView, AddToCartView, RemoveFromCartView, CancelOrderView, ChangeCartItemQuantityView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', CustomTokenObtainPairView.as_view(), name='custom_token_obtain_pair'),   
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/products/', ProductListView.as_view(), name='product-list'),
    path('api/products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('api/products/create/', ProductCreateView.as_view(), name='product-create'),
    path('api/products/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('api/products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
    path('api/cart/', CartListView.as_view(), name='cart-list'),
    path('api/cart/add/', AddToCartView.as_view(), name='cart-add'),
    path('api/cart/remove/<int:product_id>/', RemoveFromCartView.as_view(), name='cart-remove'),
    path('api/cart/change/<int:product_id>/', ChangeCartItemQuantityView.as_view(), name='change-cart-item'),
    path('api/orders/place/', PlaceOrderView.as_view(), name='place-order'),
    path('api/orders/', OrderListView.as_view(), name='order-list'),
    path('api/orders/cancel/<int:order_id>/', CancelOrderView.as_view(), name='cancel-order'),
]