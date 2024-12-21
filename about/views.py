from django.shortcuts import render
from .models import SectionOneContent, SectionTwoContent, FrequentlyAskedQuention
# Create your views here.
def about_view(request):

    section_one_details = SectionOneContent.objects.all().order_by("updated_at").first()
    section_two_details = SectionTwoContent.objects.all().order_by("updated_at").first()
    faq_list = FrequentlyAskedQuention.objects.all().order_by("updated_at")[:7]


    conext = {
        "section_one_details": section_one_details,
        "section_two_details": section_two_details,
        "faq_list": faq_list,
    }

    return render(request, "about/about.html", conext)