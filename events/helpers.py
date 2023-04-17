from django.core.mail import send_mail
import random
from django.conf import settings
from .models import (
    EventRegisterUser
)
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.utils.html import strip_tags

#generate pdf
from io import BytesIO
from xhtml2pdf import pisa
from django.http import HttpResponse
from rest_framework.response import Response
from django.template.loader import get_template
import os
#from weasyprint import HTML, BytesIO
from django.core.files.base import ContentFile




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



def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None

data = {
	"company": "Dennnis Ivanov Company",
	"address": "123 Street name",
	"city": "Vancouver",
	"state": "WA",
	"zipcode": "98663",


	"phone": "555-555-2345",
	"email": "youremail@dennisivy.com",
	"website": "dennisivy.com",
	}

#with html template
def send_success_email(email, booking_id, first_name, last_name, amount, event_for_register):

    print("event name================================================", event_for_register.event_name)

    mydict = {
        'rest_link':f"You've completed registration successfully",
        'first_name':first_name,
        'last_name':last_name,
        'location':event_for_register.location,
        'amount':amount,
        'event_name':event_for_register.event_name,
        'event_date':event_for_register.start,
        'booking_id':booking_id
    }
    html_template = 'event.html'
    html_message = render_to_string(html_template, context=mydict)
    subject = 'Registration Confirmation'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    


    user_obj = EventRegisterUser.objects.filter(email=email).last()
    pdf = render_to_pdf(html_template, mydict)

    response = HttpResponse(pdf, content_type='application/pdf')
    filename = "Event_%s.pdf" %("12341231")
    content = "attachment; filename='%s'" %(filename)
    response['Content-Disposition'] = content

    content = ContentFile(pdf.getvalue())
    user_obj.document.save(filename, content)

    user_obj.save()

    pdf_url = f"{user_obj.document.url}"
    print("PDF====================================================>",user_obj.document.url)
    
    html_message += f'<a href="http://127.0.0.1:8000{pdf_url}" style="background-color: rgb(43, 181, 240); color: white; padding: 10px; text-decoration: none;">Download Pdf</a>'

    message = EmailMessage(subject, html_message, email_from, recipient_list)
    message.content_subtype = 'html'
    message.send()
    
    user_obj = EventRegisterUser.objects.filter(email=email).last()
    print("email=====================================================", user_obj)
    user_obj.booking_id = booking_id


    
    
    user_obj.save()

    

