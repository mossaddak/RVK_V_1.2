from django.core.mail import send_mail
import random
from django.conf import settings
from .models import (
    EventRegisterUser
)
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.utils.html import strip_tags



#without html template
# def send_success_email(email):
#     subject = "Registration Confirmation"
#     registration_token = random.randint(1000,9999)
#     message = f"You've completed registration successfully"
#     email_from = settings.EMAIL_HOST
#     send_mail(subject, message, email_from, [email])
#     # user_obj = EventRegisterUser.objects.get(email=email)
#     # user_obj.token = registration_token
#     #user_obj.save()



#with html template
def send_success_email(email):
    
    otp = random.randint(1000,9999)
    mydict = {
        'rest_link':f"You've completed registration successfully"
    }
    html_template = 'event.html'
    html_message = render_to_string(html_template, context=mydict)
    subject = 'Registration Confirmation'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    message = EmailMessage(subject, html_message, email_from, recipient_list)
    message.content_subtype = 'html'
    message.send()

