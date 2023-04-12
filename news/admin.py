from django.contrib import admin
from .models import(
    NewsCategory,
    News,
    NewsBanner
)

# Register your models here.
admin.site.register(NewsCategory)
admin.site.register(News)
admin.site.register(NewsBanner)
