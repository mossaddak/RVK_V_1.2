from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import(
    Banner,
    GalleryCategory,
    Media
)


class BannerSerializer(ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'
        

class GalleryCategorySerializer(ModelSerializer):
    class Meta:
        model = GalleryCategory
        fields = '__all__'


class MediaSerializer(ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'



