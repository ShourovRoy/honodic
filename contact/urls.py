from django.urls import path
from .views import contact_us_view

app_name = "contact"
urlpatterns = [
    path('contact/', contact_us_view, name="contact_view"),
]