from django.shortcuts import render

from rest_framework.permissions import (
    BasePermission,
    SAFE_METHODS,
)

from rest_framework import(
    permissions
)
from rest_framework import (
    parsers,
)

from rest_framework.viewsets import(
    ModelViewSet
)

from .models import(
    Banner,
    GalleryCategory,
    Media
)

from .serializer import(
    BannerSerializer,
    GalleryCategorySerializer,
    MediaSerializer
)

from RVK_WEBPORTAL.permissions import (
    IsContentEditor
)


# class ReadOnlyPermission(BasePermission):
#     def has_permission(self, request, view):
#         return request.method in SAFE_METHODS
    


    
class BannerView(ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    permission_classes = [IsContentEditor]
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]


class GalleryCategoryView(ModelViewSet):
    queryset = GalleryCategory.objects.all()
    serializer_class = GalleryCategorySerializer
    permission_classes = [IsContentEditor]
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]

class MediaView(ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    permission_classes = [IsContentEditor]
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]
    