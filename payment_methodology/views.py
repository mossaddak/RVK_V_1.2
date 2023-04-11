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



# KEY_ID = "rzp_test_2y68LXTdn3DKK9"
# KEY_SECRET = "GU6RrUGnP2KId7WFSrMULPus"


KEY_ID = "rzp_test_Agj8QPGZbIlq92"
KEY_SECRET = "zzqu7LcAUJaePKW32GjesxA2"


client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))
client.set_app_details({"title": "RDK PAyment", "version": "3.2"})

print("razorpay===========================",client)





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

            DonationModel.objects.create(
                user = request.user,


                first_name = request.data.get('first_name'),
                last_name = request.data.get('last_name'),
                email = request.data.get('email'),
                phone_number = request.data.get('phone_number'),

                
                address = request.data.get('address'),

                pin_code = request.data.get('pin_code'),
                city = request.data.get('pin_code'),
                state = request.data.get('state'),
                country = request.data.get('country'),
                pan = request.data.get('pan'),

                do_you_benifited = request.data.get('do_you_benifited'),


                amount=doantation["amount"],
                payment_id=doantation["id"],
                order_date=doantation["created_at"],
                isPaid = True
            )

            mydict = {
                'username':request.user,
            }

            html_template = 'payment_success.html'
            html_message = render_to_string(html_template, context=mydict)
            subject = 'Payment Success'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.user]

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