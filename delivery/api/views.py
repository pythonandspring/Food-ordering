from django.shortcuts import render
from rest_framework import viewsets
from delivery.models import DeliveryPerson
from .serializers import DeliveryPersonSerializer

class DeliveryPersonViewSet(viewsets.ModelViewSet):
    queryset = DeliveryPerson.objects.all()
    serializer_class = DeliveryPersonSerializer
