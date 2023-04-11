from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import (
    Volunteer,
    VolunteerDescription
)




class VolunteerSerializer(ModelSerializer):
    class Meta:
        model = Volunteer
        fields = '__all__'
        

class VolunteerDescriptionSerializer(ModelSerializer):
    class Meta:
        model = VolunteerDescription
        fields = '__all__'
