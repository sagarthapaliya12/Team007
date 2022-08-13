from django.contrib import admin
from tumordetection.models import ImageModel
# Register your models here.


@admin.register(ImageModel)
class ImageModel(admin.ModelAdmin):
    list_display= ['image']