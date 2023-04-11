from rest_framework.serializers import ModelSerializer
from .models import Contact


class ContactSerailizer(ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'