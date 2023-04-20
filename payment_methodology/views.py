from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view
from .serializer import (
    DonationSerializer
)
from rest_framework.viewsets import(
    ModelViewSet
)

from .models import (
    DonationModel
)


import json

import environ
import razorpay
from django.conf import settings 
from django.template.loader import render_to_string
from django.core.mail import EmailMessage



#pdf
#generate pdf
from io import BytesIO
from xhtml2pdf import pisa
from django.http import HttpResponse
from rest_framework.response import Response
from django.template.loader import get_template
import os
#from weasyprint import HTML, BytesIO
from django.core.files.base import ContentFile



# KEY_ID = "rzp_test_2y68LXTdn3DKK9"
# KEY_SECRET = "GU6RrUGnP2KId7WFSrMULPus"


KEY_ID = "rzp_test_Agj8QPGZbIlq92"
KEY_SECRET = "zzqu7LcAUJaePKW32GjesxA2"


client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))
client.set_app_details({"title": "RDK PAyment", "version": "3.2"})

print("razorpay===========================",client)

def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None



class DonateView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    
    def post(self, request):

        try:
            donation_model = DonationModel.objects.all()
            serializer = DonationSerializer(donation_model, many=True)
            
            KEY_ID = "rzp_test_2y68LXTdn3DKK9"
            KEY_SECRET = "GU6RrUGnP2KId7WFSrMULPus"

            client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))
            
            amount = request.data.get('amount')
            currency = "INR"


            data = {"amount": int(amount)*100, "currency": currency}
            doantation = client.order.create(data=data)
            print(doantation["id"])

            first_name = request.data.get('first_name')
            last_name = request.data.get('last_name')
            amount=doantation["amount"]
            payment_id = doantation["id"]
            pan = request.data.get('pan')
            address = request.data.get('address')
            DonationModel.objects.create(
                user = request.user,
                first_name = first_name,
                last_name = last_name,
                email = request.data.get('email'),
                phone_number = request.data.get('phone_number'),
                address = address,
                pin_code = request.data.get('pin_code'),
                city = request.data.get('pin_code'),
                state = request.data.get('state'),
                country = request.data.get('country'),
                pan = pan,

                do_you_benifited = request.data.get('do_you_benifited'),


                amount=amount,
                payment_id=payment_id,
                order_date=doantation["created_at"],
                isPaid = True
            )

            mydict = {
                'username':request.user,
                'first_name':first_name,
                'last_name':last_name,
                'amount':amount/100,
                'payment_id':payment_id,
                'pan':pan,
                'address':address
            }

            html_template = 'payment_success.html'
            html_message = render_to_string(html_template, context=mydict)
            subject = 'Payment Success'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.data.get('email')]

            user_email = request.user.email
            user_obj = DonationModel.objects.filter(email=user_email).last()
            print("DNobj================================================",user_email)
            pdf = render_to_pdf(html_template, mydict)
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Donation_%s.pdf" %("12341231")
            content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            content = ContentFile(pdf.getvalue())
            user_obj.document.save(filename, content)
            user_obj.save()

            pdf_url = f"{user_obj.document.url}"
            print("PDF====================================================>",user_obj.document.url)
            
            html_message += f'<a href="http://127.0.0.1:8000{pdf_url}" style="background-color: rgb(43, 181, 240); color: white; padding: 10px; text-decoration: none;">Download Pdf</a>'


            message = EmailMessage(subject, html_message, email_from, recipient_list)
            #send_mail(subject, html_message, email_from, recipient_list)
            message.content_subtype = 'html'
            message.send()  

            print("#User========================================",recipient_list)


            return Response({
                "message":"Thank For Donation",
                "donation details": int(doantation["amount"])/100,
                "amount":doantation["amount"],
                "payment_id":doantation["id"],
                "order_date":doantation["created_at"],
                "is_pay":True
            }
                
            )
        except Exception as e:
            return Response({
                "message":"somthing wrong with payment",
                "error":e
            }
        )
    
    def get(self, request):
        all_donation = DonationModel.objects.all()
        serializer = DonationSerializer(all_donation, many=True)
        perm = request.user.groups.filter(name='Finance Department').exists()
        print(all_donation)

        if request.user.is_authenticated and perm:
            return Response(
                {
                "data":(serializer.data)
                },status.HTTP_200_OK
            
            )
        else:
             return Response(
                  {
                    "message":"you don't have permission for this action"
                  },status.HTTP_200_OK
            )
