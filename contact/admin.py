from django.contrib import admin
from .models import ContactMessage, ContactDetail
# Register your models here.

class AdminContactMessage(admin.ModelAdmin):
    list_display = ['first_name', 'email', 'subject', 'is_completed', 'created_at']
    search_fields = ['subject', 'first_name', 'last_name', 'email', 'is_completed']
    list_filter = ['created_at', 'updated_at', 'is_completed']

admin.site.register(ContactMessage, AdminContactMessage)
admin.site.register(ContactDetail)
