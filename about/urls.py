from django.urls import path
from .views import about_view

app_name = 'about'
urlpatterns = [
    path('about/', about_view, name="about_view")
]