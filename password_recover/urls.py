from django.urls import path
from password_recover.views import (
    PasswordReset,
    ResetPasswordAPI
)



urlpatterns = [
    path('reset-password/', PasswordReset.as_view(), name="request-password-reset/"),
    path('reset-password/<str:encoded_pk>/<str:token>/',ResetPasswordAPI.as_view(), name="reset-password"),
    
]