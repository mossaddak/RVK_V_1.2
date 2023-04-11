from rest_framework.serializers import ModelSerializer
from .models import(
    PremRawatAboutBanner,
    PremRawattDescription
)

class PremRawatAboutBannerSerializer(ModelSerializer):
    class Meta:
        model = PremRawatAboutBanner
        fields = '__all__'
        

class PremRawattDescriptionSerializer(ModelSerializer):
    class Meta:
        model = PremRawattDescription
        fields = '__all__'
