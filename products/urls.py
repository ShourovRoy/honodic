from django.urls import path
from .views import ProductsView, product_view

app_name = "products"
urlpatterns = [
    path('products/', ProductsView, name="products_view"),
    path('products/details/<int:product_id>/', product_view, name="product_view")
]