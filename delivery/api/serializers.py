from rest_framework import serializers
from delivery.models import deliveryUser, Feedback, Contact

class DeliveryUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = deliveryUser
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
