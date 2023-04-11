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
from .models import (
    RvkAboutBanner,
    RvkAboutDescription,
    QuickLinks
)
from .serializer import (
    RvkAboutBannerSerializer,
    RvkAboutDescriptionSerializer,
    QuickLinksSerializer
)

from RVK_WEBPORTAL.permissions import (
    IsContentEditor
)







# Create your views here.
# class ReadOnlyPermission(BasePermission):
#     def has_permission(self, request, view):
#         return request.method in SAFE_METHODS
    
class RvkAboutBannerView(ModelViewSet):
    queryset = RvkAboutBanner.objects.all()
    serializer_class = RvkAboutBannerSerializer
    permission_classes = [IsContentEditor]


class RvkAboutDescriptionView(ModelViewSet):
    queryset = RvkAboutDescription.objects.all()
    serializer_class = RvkAboutDescriptionSerializer
    permission_classes = [IsContentEditor]

class QuickLinksView(ModelViewSet):
    queryset = QuickLinks.objects.all()
    serializer_class = QuickLinksSerializer
    permission_classes = [IsContentEditor]
    

