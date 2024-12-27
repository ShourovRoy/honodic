from django.shortcuts import render
from .models import Product, Category
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
# Create your views here.

class ProductsView(ListView):
    template_name = "products/products.html"
    ordering = ['updated_at']
    model = Product
    context_object_name = "products"

    def get_queryset(self):

        qs = super().get_queryset()
        category_id = self.request.GET.get("category_id")

        if category_id:
            category = get_object_or_404(Category, pk=int(category_id))
            qs = category.products.all().order_by("created_at")
        
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all().order_by("updated_at")
        return context

# product details view
class ProductView(DetailView):
    template_name = "products/product_details.html"
    model = Product
    context_object_name = "product_details"


    def get_object(self, queryset = None):
        product_id = self.kwargs['product_id']
        return get_object_or_404(self.model, pk=product_id)
