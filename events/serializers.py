from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import (
    Event,
    EventRegisterUser
)
from accounts.serializers import UserGetSerializer

from accounts.serializers import(
    UserSerializer
)

class EventSerializer(ModelSerializer):
    
    class Meta:
        model = Event
        fields = '__all__'

class EventRegisterSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = EventRegisterUser 
        fields = '__all__' 



