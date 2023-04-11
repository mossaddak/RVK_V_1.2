from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TicketSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Ticket

class SupportViewset(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated,]


    def get_queryset(self):
        if self.request.user.is_superuser:
            return Ticket.objects.all()
        else:
            return Ticket.objects.filter(user=self.request.user)
