from django.shortcuts import render
from .models import ContactMessage
from django.contrib import messages
from .forms import ContactForm
from django.views.generic import FormView

# Create your views here.


class ContactUsView(FormView):
    template_name = "contact/contact.html"
    success_url = "/contact/"
    form_class = ContactForm

    def form_valid(self, form):
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
            messages.success(self.request, "Thanks for contacting us. We will get back to you soon.")
            
        except Exception as e:
            print("error: ",str(e)) 
            messages.error(self.request, "Faild to send the message.")


        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Please correct the errors in the form.")
        return super().form_invalid(form)
    
