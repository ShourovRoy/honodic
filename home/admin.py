from django.contrib import admin
from .models import Slider, AboutDetail, UniqueFeature, FeaturedProductDetail
# Register your models here.



class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated_at', 'created_at']

admin.site.register(Slider, SliderAdmin)
admin.site.register(AboutDetail)


class UniqueFeatureAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated_at', 'created_at']

admin.site.register(UniqueFeature, UniqueFeatureAdmin)


admin.site.register(FeaturedProductDetail)