from django.contrib import admin
from .models import(
    RvkAboutBanner,
    RvkAboutDescription,
    QuickLinks
)

# Register your models here.
admin.site.register(RvkAboutBanner)
admin.site.register(RvkAboutDescription)
admin.site.register(QuickLinks) 
