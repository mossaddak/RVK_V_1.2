from django.contrib import admin
from .models import(
    Media,
    GalleryCategory,
    Banner
)

# Register your models here.
admin.site.register(Media)
admin.site.register(GalleryCategory)
admin.site.register(Banner)

