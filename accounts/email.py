from django.core.mail import send_mail
import random
from django.conf import settings
from .models import (
    User
)
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.utils.html import strip_tags



#without html template
# def send_otp_via_email(email):
#     subject = "Your account verification email"
#     otp = random.randint(1000,9999)
#     message = f"Your otp is {otp}"
#     email_from = settings.EMAIL_HOST
#     send_mail(subject, message, email_from, [email])
#     user_obj = User.objects.get(email=email)
#     user_obj.otp = otp
#     user_obj.save()



#with html template
def send_otp_via_email(email):
    
    otp = random.randint(1000,9999)
    mydict = {
        'otp':f"{otp}"
    }
    html_template = 'verified_emaii_otp.html'
    html_message = render_to_string(html_template, context=mydict)
    subject = 'Account Verification OTP'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    message = EmailMessage(subject, html_message, email_from, recipient_list)
    message.content_subtype = 'html'
    message.send()

    user_obj = User.objects.get(email=email)
    user_obj.otp = otp
    user_obj.save()


