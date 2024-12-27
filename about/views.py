from django.shortcuts import render
from .models import SectionOneContent, SectionTwoContent, FrequentlyAskedQuention
from django.views.generic.base import TemplateView 

# Create your views here.
class AboutView(TemplateView):
    template_name = "about/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['section_one_details'] = SectionOneContent.objects.all().order_by("updated_at").first()
        context['section_two_details'] = SectionTwoContent.objects.all().order_by("updated_at").first()
        context['faq_list'] = FrequentlyAskedQuention.objects.all().order_by("updated_at")[:7]

        return context; 