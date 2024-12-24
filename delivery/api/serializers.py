from rest_framework import serializers
from delivery.models import DeliveryPerson,deliveryUser, Feedback, Contact

class DeliveryPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryPerson
        fields = '__all__'

class DeliveryUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = deliveryUser
        fields = '__all__'

class Feedback_dSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

class Contact_dSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

