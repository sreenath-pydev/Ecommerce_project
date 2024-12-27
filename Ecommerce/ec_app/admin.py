from django.contrib import admin
from .models import Customer, Product

# Register the Customer model
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'phone', 'delete_status', 'created_at', 'updated_at')
    list_filter = ('delete_status', 'city', 'created_at')
    search_fields = ('name', 'address', 'locality', 'phone')

# Register the Product model
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'priority', 'delete_status', 'created_at', 'updated_at')
    list_filter = ('delete_status', 'priority', 'created_at')
    search_fields = ('title', 'description')
