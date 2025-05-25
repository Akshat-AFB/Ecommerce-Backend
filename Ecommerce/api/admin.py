from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Product, Order, CartItem, Cart, OrderItem

# Extend UserAdmin to include 'role' in admin panel
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Role Info', {'fields': ('role',)}),
    )
    list_display = ('username', 'email', 'role', 'is_staff', 'is_superuser')


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('product', 'quantity', 'price_at_order_time')

admin.site.register(User, UserAdmin)
admin.site.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
admin.site.register(CartItem)
admin.site.register(OrderItem)
admin.site.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'order_status', 'order_date')
    list_filter = ('order_status', 'order_date')
    inlines = [OrderItemInline]
admin.site.register(Cart)
