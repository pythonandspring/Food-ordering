from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from customer.models import customerUser,Feedback,Contact
from .serializers import CustomerSerializer,FeedbackSerializer,ContactSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication



# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = customerUser.objects.all()
    serializer_class = CustomerSerializer
    

class FeedbackViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class ContactViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
