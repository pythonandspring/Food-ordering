from rest_framework import serializers
from delivery.models import DeliveryPerson

class DeliveryPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryPerson
        fields = '__all__'
