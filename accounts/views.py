from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import(
    UserSerializer,
    VeriFyAccountSerializer,
    LoginSerializer
)
from rest_framework import status

from .models import (
    User
)
import uuid
from django.core.mail import send_mail
from .models import(
    UserVerification
)
from django.conf import settings
from .email import *


#User = get_user_model()

def send_mail_after_registration(email , token):
    subject = 'Your accounts need to be verified'
    message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list)

    return Response(
        {
            'message':"check you mail",
            'data':message
        },status = status.HTTP_201_CREATED
    )

class AccountViewSet(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = UserSerializer(data=data)
            if not serializer.is_valid():
                return Response(
                    {
                        'message':"something Went Wrong",
                        'data':serializer.errors
                    },status = status.HTTP_400_BAD_REQUEST
                )
            if serializer.is_valid():

                serializer.save()

                
                return Response(
                    {
                        
                        'message':"Your account is created, to verify check your mail. An email is sent.",
                        'data':serializer.data,
                        'mail':send_otp_via_email(serializer.data['email']),
                    },status = status.HTTP_201_CREATED
                )
        

        except Exception as e:
            print(e)
            return Response(
                    {
                        'message':"something Went Wrong",
                        'message':serializer.errors,
                    },status = status.HTTP_400_BAD_REQUEST
                    
                )

    def get(self, request):

        eventregister_model = User.objects.all()
        serializer = UserSerializer(eventregister_model, many=True)
        return Response(
            {
                'data':serializer.data,
                'message':"Your account is created"
            },status = status.HTTP_201_CREATED
        )
    

class VerifyOTPview(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = VeriFyAccountSerializer(data=data)
            
            if serializer.is_valid():
                email = serializer.data['email']
                otp = serializer.data['otp']

                user = User.objects.filter(email=email)

                

                if not user.exists():
                    return Response(
                        {
                            'message':"You didn't create account yet, please create an account",
                            'error':"User not found"
                        },status = status.HTTP_404_NOT_FOUND
                    )
                
                if not user[0].otp == otp:
                    return Response(
                        {
                            'message':"Please give here correct OTP",
                            'error':"Wront OTP"
                        },status = status.HTTP_404_NOT_FOUND
                    )
                

                user = user[0]
                if user.verified == False:
                
                    user.verified = True
                    user.save()

                    #print("OTPemail=====================================",user[0].verified)

                    return Response(
                        {
                            'message':"Your account is verified now.",
                            'data':serializer.data
                        },status = status.HTTP_201_CREATED
                    )
                else:
                    return Response(
                        {
                            'message':"Your already verified your account"
                        },status = status.HTTP_201_CREATED
                    )

            
        except Exception as e:
            print("Error=======================================", e)



class LoginView(APIView):
    def post(self, request):
        
        
        try:
            data = request.data
            serializer = LoginSerializer(data=data)

            if not serializer.is_valid():
                return Response(
                    {
                        'data':serializer.errors,
                        'message':"something Went Wrong"
                    },status = status.HTTP_400_BAD_REQUEST
                    
                )
            response = serializer.get_jwt_token(serializer.data)
            return Response(response,status = status.HTTP_200_OK)
        
        except Exception as e:
            print("error=================",e)
            return Response(
                    {
                        'data':{},
                        'message':"something Went Wrong"
                    },status = status.HTTP_400_BAD_REQUEST
                    
                )
