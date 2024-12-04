from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from delivery.models import deliveryUser, Feedback, Contact
from delivery.api.serializers import DeliveryUserSerializer, FeedbackSerializer, ContactSerializer

class DeliveryUserViewSet(viewsets.ModelViewSet):
    queryset = deliveryUser.objects.all()
    serializer_class = DeliveryUserSerializer
    # permission_classes = [IsAuthenticated]  # Only authenticated users can access

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

