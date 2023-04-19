from rest_framework.views import (
    APIView
)
from rest_framework.permissions import (
    IsAuthenticated
)
from rest_framework_simplejwt.authentication import (
    JWTAuthentication
)
from .serializers import (
    EventSerializer,
    EventRegisterSerializer
)
from rest_framework import viewsets
from .models import (
    Event,
    EventRegisterUser
)

from rest_framework import (
    parsers,
) 
from RVK_WEBPORTAL.permissions import(
    IsHR,
    RegistrationLimit,
    IsFinance
)
import razorpay
from rest_framework.response import Response
from accounts.models import(
    User
)
from django.shortcuts import get_object_or_404

from events.helpers import(
    send_success_email
)
import random
from rest_framework import status



class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by("-created_at")
    serializer_class = EventSerializer
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]
    permission_classes = [IsHR]


class EventRegisterViewSet(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def post(self, request):
        #TotallRegisterUser = EventRegisterUser.objects.all().count()
        EventCapacity = Event.objects.last().capacity

        register_user_mail = request.user.email
        print("REQUESTuser===========================================================", request.user.email)
        try:

            eventregister_model = EventRegisterUser.objects.all()
            serializer = EventRegisterSerializer(eventregister_model, many=True)

            is_pay = request.data.get('is_pay')

            event_id = request.data.get('event_id')

            all_events = Event.objects.all()
            event_for_register = get_object_or_404(all_events, pk=event_id)
            #print(event_register["id"]) 
            event_price = event_for_register.event_price
            print("Testing event price==========================================",event_for_register.event_price)

            TotallRegisterUser = event_for_register.user.all().count()
            events = event_for_register.user.all()

            if request.user in event_for_register.user.all():
                print("Update")

                return Response({
                        "message":"You already registered for this event."
                    }, status=status.HTTP_200_OK
                
                )
            else:
                if TotallRegisterUser <= EventCapacity:
                    amount = 0
                    booking_id = random.randint(1000000,9999999)

                    
                    if event_price == None:
                        try:
                            first_name = request.data.get('first_name')
                            last_name = request.data.get('last_name')
                            amount = "Free"
                            print("TestinEmail=====================================>", request.user.email)
                            EventRegisterUser.objects.create(
                                event = event_for_register,
                                user = request.user,
                                first_name = first_name,
                                last_name = last_name,
                                email = request.user.email,
                                phone_number = request.data.get('phone_number'),
                                smart_card_number = request.data.get('smart_card_number'),
                                address = request.data.get('address'),
                                pin_code = request.data.get('pin_code'),
                                city = request.data.get('pin_code'),
                                state = request.data.get('state'),
                                country = request.data.get('country'),
                                is_pay = request.data.get('amount'),
                                amount="0",
                                booking_id = booking_id
                            )
                            send_success_email(register_user_mail, booking_id, first_name, last_name, amount, event_for_register)
                        except Exception as e:
                            return Response({
                                    "message":"All field required",
                                    "error":e
                                }
                            )
                        event_for_register.user.add(request.user)
                        return Response({
                                "message":"Thank For Registration",
                                "is_pay":False
                            }, status=status.HTTP_201_CREATED
                        )
                    else:

                        # KEY_ID = "rzp_test_2y68LXTdn3DKK9"
                        # KEY_SECRET = "GU6RrUGnP2KId7WFSrMULPus"

                        KEY_ID = "rzp_test_Agj8QPGZbIlq92"
                        KEY_SECRET = "zzqu7LcAUJaePKW32GjesxA2"

                        client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))
                        currency = "INR"
                        #amount = request.data.get('amount')
                        print("Event price=================================>", event_price)
                        data = {"amount": int(event_price)*100, "currency": currency}
                        event_register = client.order.create(data=data)
                        
                        try:
                            first_name = request.data.get('first_name')
                            last_name = request.data.get('last_name')
                            amount = event_register["amount"]/100
                            EventRegisterUser.objects.create(
                                event = event_for_register,
                                user = request.user,
                                first_name = first_name,
                                last_name = last_name,
                                email = request.user.email,
                                phone_number = request.data.get('phone_number'),
                                smart_card_number = request.data.get('smart_card_number'),
                                address = request.data.get('address'),
                                pin_code = request.data.get('pin_code'),
                                city = request.data.get('pin_code'),
                                state = request.data.get('state'),
                                country = request.data.get('country'),
                                card_details = request.data.get('card_details'),
                                amount=event_price,
                                payment_id=event_register["id"],
                                order_date=event_register["created_at"],
                                is_pay = True
                            )
                            send_success_email(register_user_mail, booking_id, first_name, last_name, amount, event_for_register)
                        except Exception as e:
                            return Response({
                                    "message":"All field required",
                                    "error":e,
                                    
                                }
                            )
                        event_for_register.user.add(request.user)
                        return Response({
                                "message":"Thank For Registration",
                                "donation details": int(event_register["amount"])/100,
                                "amount":event_register["amount"],
                                "payment_id":event_register["id"],
                                "card_details":request.data.get('card_details'),
                                "is_pay":True
                            },status=status.HTTP_201_CREATED
                        )
                    
                return Response({
                        "message":"You can't register at the moment, event registration capacity is already over."
                    }, status=status.HTTP_200_OK
                )
        except Exception as e:
             return Response({
                    "message":"somthing wrong with payment",
                    "error":e
                },status=status.HTTP_400_BAD_REQUEST
            )
            
        

    def get(self,request):
        eventregister_model = EventRegisterUser.objects.all()
        serializer = EventRegisterSerializer(eventregister_model, many=True)


        if request.user.groups.filter(name='Finance Department').exists():
            return Response(
                {
                    "message":"data fetch successfully",
                    "data":serializer.data
                }
            )
        else:
            return Response(
                {
                    "message":"You don't have permission"
                }
            )
        
class EventRegisterForFinanceViewSet(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    


