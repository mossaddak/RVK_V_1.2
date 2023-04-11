from django.shortcuts import render
from .serializers import (
    VolunteerSerializer,
    VolunteerDescriptionSerializer
)
from rest_framework import viewsets
from .models import (
    Volunteer,
    VolunteerDescription
)

from rest_framework.permissions import (
    BasePermission, SAFE_METHODS
)
from rest_framework import (
    parsers,
)

from rest_framework.viewsets import(
    ModelViewSet
)


from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny

from RVK_WEBPORTAL.permissions import (
    IsContentEditor
)


# class ReadOnlyPermission(BasePermission):
#     def has_permission(self, request, view):
#         return request.method in SAFE_METHODS



class VolunteerViewset(viewsets.ModelViewSet):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    permission_classes = [AllowAny]

class NewsModelView(ModelViewSet):
    serializer_class = VolunteerDescriptionSerializer
    queryset = VolunteerDescription.objects.all()
    permission_classes = [IsContentEditor]
   