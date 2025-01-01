from .models import Slider, AboutDetail, UniqueFeature, FeaturedProductDetail, Statement
from products.models import Product
from django.views.generic.base import TemplateView
# Create your views here.


class HomeView(TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        statement = Statement.objects.first()

        context['sliders'] = Slider.objects.all().order_by("-updated_at")[:3]
        context['statement'] = statement
        context['about_information'] = AboutDetail.objects.first()
        context['unique_features'] = UniqueFeature.objects.all().order_by("-updated_at")[:4]
        context['featured_product_list'] = Product.objects.filter(is_featured=True).order_by("updated_at")[:3]
        context['featured_product_details'] = FeaturedProductDetail.objects.first()

        return context