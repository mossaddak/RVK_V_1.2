from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import (
    DonationModel
)

class DonationSerializer(ModelSerializer):
    class Meta:
        model = DonationModel
        fields = "__all__"


