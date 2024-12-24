from django.shortcuts import render
from rest_framework import viewsets
from delivery.models import DeliveryPerson, deliveryUser, Feedback, Contact
from delivery.api.serializers import DeliveryPersonSerializer, DeliveryUserSerializer, Feedback_dSerializer, Contact_dSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class DeliveryPersonViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = DeliveryPerson.objects.all()
    serializer_class = DeliveryPersonSerializer

class DeliveryUserViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = deliveryUser.objects.all()
    serializer_class = DeliveryUserSerializer

class Feedback_dViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Feedback.objects.all()
    serializer_class = Feedback_dSerializer

class Contact_dViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Contact.objects.all()
    serializer_class = Contact_dSerializer
