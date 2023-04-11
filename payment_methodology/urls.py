from django.urls import path
from payment_methodology.views import(
    DonateView
)


urlpatterns = [
    path('donate/', DonateView.as_view(), name='donate'),
]