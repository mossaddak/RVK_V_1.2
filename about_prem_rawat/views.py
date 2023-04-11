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
    PremRawatAboutBanner,
    PremRawattDescription
)

from .serializer import (
    PremRawatAboutBannerSerializer,
    PremRawattDescriptionSerializer
)


from RVK_WEBPORTAL.permissions import (
    IsContentEditor
)



# Create your views here.
# class ReadOnlyPermission(BasePermission):
#     def has_permission(self, request, view):
#         return request.method in SAFE_METHODS


class PremRawatAboutBannerView(ModelViewSet):
    queryset = PremRawatAboutBanner.objects.all()
    serializer_class = PremRawatAboutBannerSerializer
    permission_classes = [IsContentEditor]


class PremRawattDescriptionView(ModelViewSet):
    queryset = PremRawattDescription.objects.all()
    serializer_class = PremRawattDescriptionSerializer
    permission_classes = [IsContentEditor]


