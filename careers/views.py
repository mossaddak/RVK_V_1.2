from django.shortcuts import render
from .serializers import (
    CareerSerailizer,
    CareerDescriptionSerailizer
)
from rest_framework import viewsets
from .models import (
    Career,
    CareerDescription
)
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser

from rest_framework.permissions import (
    BasePermission, SAFE_METHODS
)

from RVK_WEBPORTAL.permissions import(
    IsContentEditor,
    IsHR
)




# class ReadOnlyPermission(BasePermission):
#     def has_permission(self, request, view):
#         return request.method in SAFE_METHODS

class CareerViewset(viewsets.ModelViewSet):
    queryset = Career.objects.all()
    serializer_class = CareerSerailizer
    #filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    parser_classes = [MultiPartParser]
    permission_classes = [IsHR]

class CareerDescModelView(viewsets.ModelViewSet):
    queryset = CareerDescription.objects.all()
    serializer_class = CareerDescriptionSerailizer
    permission_classes = [IsContentEditor]


   