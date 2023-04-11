from django.contrib import admin
from .models import(
    Banner,
    LatestVideo,
    # Initiative,
    NewsShelter
)

# Register your models here.
admin.site.register(Banner)
admin.site.register(LatestVideo)
# admin.site.register(Initiative)
admin.site.register(NewsShelter)