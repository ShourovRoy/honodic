from .models import ContactDetail


# admin contact
def contact_details(request):
    try:
        contact_details = ContactDetail.objects.get();
    except: 
        contact_details = None

    context = {
        "contact_details": contact_details 
    }

    return context