from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import (
    Career,
    CareerDescription
)



class CareerSerailizer(ModelSerializer):
    class Meta:
        model = Career
        fields = '__all__'

class CareerDescriptionSerailizer(ModelSerializer):
    class Meta:
        model = CareerDescription
        fields = '__all__'