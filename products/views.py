from django.shortcuts import render
from .models import Product, Category
from django.shortcuts import get_object_or_404
# Create your views here.

def ProductsView(request):

    products = Product.objects.all().order_by("updated_at")
    categories = Category.objects.all().order_by("updated_at")

    category_id = request.GET.get("category_id")

    if category_id:
        category_obj = get_object_or_404(Category, pk=category_id)
        products = category_obj.products.all()

    context = {
        "products": products,
        "categories": categories
    }

    return render(request, 'products/products.html', context)


# product details view
def product_view(request, product_id):

    product_details = get_object_or_404(Product, pk=product_id)


    context = {
        "product_details": product_details 
    }

    return render(request, "products/product_details.html", context)