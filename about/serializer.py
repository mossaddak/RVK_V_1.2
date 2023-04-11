from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import (
    RvkAboutBanner,
    RvkAboutDescription,
    QuickLinks
)




class RvkAboutBannerSerializer(ModelSerializer):
    class Meta:
        model = RvkAboutBanner
        fields = '__all__'
        

class RvkAboutDescriptionSerializer(ModelSerializer):
    class Meta:
        model = RvkAboutDescription
        fields = '__all__'


class QuickLinksSerializer(ModelSerializer):
    class Meta:
        model = QuickLinks
        fields = '__all__'
