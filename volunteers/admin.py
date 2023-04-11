from django.contrib import admin
from .models import (
    Volunteer,
    VolunteerDescription
)


admin.site.register(Volunteer)
admin.site.register(VolunteerDescription)
