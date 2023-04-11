from rest_framework.serializers import ModelSerializer
from .models import(
    Banner,
    LatestVideo,
    NewsShelter
)

class BannerSerializer(ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__" 

class LatestVideoSerializer(ModelSerializer):
    class Meta:
        model = LatestVideo
        fields = "__all__" 

class NewsShelterSerializer(ModelSerializer):
    class Meta:
        model = NewsShelter
        fields = "__all__"


