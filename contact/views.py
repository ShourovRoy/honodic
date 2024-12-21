from django.shortcuts import render
from .models import ContactMessage
from django.contrib import messages
from .forms import ContactForm


# Create your views here.


def contact_us_view(request):

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]

            try:
                ContactMessage(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    subject=subject,
                    message=message,
                ).save();
                messages.success(request, "Thanks for contacting us. We will get back to you soon.")
            
            except: 
                messages.error(request, "Faild to send the message.")
    else: 
        form = ContactForm()

    context = {
        "form": form
    }

    return render(request, "contact/contact.html", context)
