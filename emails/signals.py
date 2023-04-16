from django.db.models.signals import post_save
from django.dispatch import receiver
from .utils import send_email
from django.contrib.auth import get_user_model
from accounts.models import UserVerification

User = get_user_model()
#nice

@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    if created:

        user_verification = UserVerification.objects.create(user=instance)
        
        subject = "Account Verification"


        send_email(email_type="user_verification_email", subject=subject, recipients=["namangalabernard@gmail.com", ], object=instance, token=user_verification.token)