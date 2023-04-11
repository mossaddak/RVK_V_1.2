from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import(
    UserSerializer
)
from rest_framework import status

from .models import (
    User
)


#User = get_user_model()

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
            serializer.save()

            
            return Response(
                {
                    'message':"Your account is created",
                    'data':serializer.data
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

