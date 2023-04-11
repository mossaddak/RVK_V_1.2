from django.contrib import admin
from .models import (
    Event,
    EventRegisterUser,
    
)


admin.site.register(Event)
admin.site.register(EventRegisterUser) 