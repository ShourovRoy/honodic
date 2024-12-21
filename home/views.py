from django.shortcuts import render
from .models import Slider, AboutDetail, UniqueFeature, FeaturedProductDetail
from products.models import Product
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def home_view(request):

    sliders = Slider.objects.all().order_by("-updated_at")[:3]
    try:
        about_information = AboutDetail.objects.get()
    except ObjectDoesNotExist:
        about_information = None
    unique_features = UniqueFeature.objects.all().order_by("-updated_at")[:4]
    featured_product_list = Product.objects.filter(is_featured=True).order_by("updated_at")[:3]

    try:
        featured_product_details = FeaturedProductDetail.objects.get()
    except ObjectDoesNotExist:
        featured_product_details = None
    


    context = {
        "sliders": sliders,
        "about_information": about_information, 
        "unique_features": unique_features,
        "featured_product_list": featured_product_list,
        "featured_product_details": featured_product_details,
    }
    
    return render(request, 'home/home.html', context)