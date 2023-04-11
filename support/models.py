from django.db import models
from django.contrib.auth import get_user_model
from .constants import SUPPORT_CHOICES


User = get_user_model()


class Ticket(models.Model):
    description = models.TextField()
    status = models.CharField(choices=SUPPORT_CHOICES, max_length=25)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ticket_owner")