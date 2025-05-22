from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Product, Order, CartItem

# Extend UserAdmin to include 'role' in admin panel
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Role Info', {'fields': ('role',)}),
    )
    list_display = ('username', 'email', 'role', 'is_staff', 'is_superuser')

admin.site.register(User, UserAdmin)
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Order)
