from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from delivery.models import deliveryUser, Feedback, Contact
from delivery.api.serializers import DeliveryUserSerializer, FeedbackSerializer, ContactSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class DeliveryUserViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = deliveryUser.objects.all()
    serializer_class = DeliveryUserSerializer
    # permission_classes = [IsAuthenticated]  # Only authenticated users can access

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

