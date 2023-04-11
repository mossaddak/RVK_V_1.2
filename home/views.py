from django.shortcuts import render
from rest_framework.permissions import (
    BasePermission, SAFE_METHODS
)
from rest_framework import (
    parsers,
)

from rest_framework.viewsets import(
    ModelViewSet
)
from .models import(
    Banner,
    LatestVideo,
    NewsShelter

)
from .serializer import(
    BannerSerializer,
    LatestVideoSerializer,
    NewsShelterSerializer
)

from RVK_WEBPORTAL.permissions import(
    IsContentEditor
)
from rest_framework import permissions

from RVK_WEBPORTAL.permissions import(
    AdminAccessOnlyOtherCanSee
)

class ReadOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

# Create your views here.
class BannerModelView(ModelViewSet):

    serializer_class = BannerSerializer
    queryset = Banner.objects.all()
    permission_classes = [IsContentEditor]

    print("BannerSerializer=====================================")

    parser_classes = [parsers.FormParser, parsers.MultiPartParser]

class LatestVideoModelView(ModelViewSet):

    serializer_class = LatestVideoSerializer
    queryset = LatestVideo.objects.all()
    permission_classes = [IsContentEditor]



class NewsShelterViewset(ModelViewSet):

    serializer_class = NewsShelterSerializer
    queryset = NewsShelter.objects.all()
    permission_classes = [AdminAccessOnlyOtherCanSee]
