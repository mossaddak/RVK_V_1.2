from django.urls import path,include
from .views import(
    EventRegisterViewSet
)
urlpatterns = [
    path('event_register/', EventRegisterViewSet.as_view(), name="event_register")
]