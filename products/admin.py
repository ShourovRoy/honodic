from django.contrib import admin
from .models import Product
# Register your models here.




class ProductAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_filter = ['title', 'is_featured', 'categories', 'created_at', 'updated_at']
    list_display = ['title', 'is_featured', 'updated_at', 'created_at']


admin.site.register(Product, ProductAdmin)
