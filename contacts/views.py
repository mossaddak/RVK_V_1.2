from django.shortcuts import render
from .serializers import ContactSerailizer
from rest_framework import viewsets
from .models import Contact
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny


class ContactViewset(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerailizer
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    permission_classes = [AllowAny]


   