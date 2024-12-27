from django.urls import path
from .views import ProductsView, ProductView

app_name = "products"
urlpatterns = [
    path('products/', ProductsView.as_view(), name="products_view"),
    path('products/details/<int:product_id>/', ProductView.as_view(), name="product_view")
]