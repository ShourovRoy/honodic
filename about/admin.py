from django.contrib import admin
from .models import SectionOneContent, SectionTwoContent, FrequentlyAskedQuention
# Register your models here.


class AdminSectionOneContent(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']
    list_filter = ['title', 'created_at', 'updated_at']
    search_fields = ['title', 'desc', 'sub_title']

admin.site.register(SectionOneContent, AdminSectionOneContent)

class AdminSectionTwoContent(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']
    list_filter = ['title', 'created_at', 'updated_at']
    search_fields = ['title', 'desc']



admin.site.register(SectionTwoContent, AdminSectionTwoContent)

class AdminFrequentlyAskedQuention(admin.ModelAdmin):
    list_filter = ['created_at', 'updated_at']
    search_fields = ['title', 'desc']
    list_display = ['title', 'created_at', 'updated_at']


admin.site.register(FrequentlyAskedQuention, AdminFrequentlyAskedQuention)