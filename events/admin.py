from django.contrib import admin
from .models import (
    Event,
    EventRegisterUser,
    
)

class PurchasedItemAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "event_name",
        "host_name",
        "event_price"
    )



admin.site.register(Event, PurchasedItemAdmin)
admin.site.register(EventRegisterUser) 