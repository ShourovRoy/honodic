from .models import FooterTitle


def FooterTitleProcessor(request):
    footer_title = FooterTitle.objects.first();

    context = {
        "footer_title": footer_title 
    }

    return context