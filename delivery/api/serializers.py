from rest_framework import serializers
from customer.models import Place
from delivery.models import DeliveryPerson,deliveryUser, Feedback, Contact, DeliveryPersonLocation

class DeliveryPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryPerson
        fields = '__all__'
    

class DeliveryUserSerializer(serializers.ModelSerializer):
    # Fields to be included in the serializer
    
    class Meta:
        model = deliveryUser
        fields = [
            'id', 'username', 'email', 'is_superuser', 'name', 'state', 'city', 'place', 
            'latitude', 'longitude', 'address' ,'password', 'is_staff', 
            'is_active', 'date_joined', 'last_login', 'is_user', 
            'is_restaurant', 'is_delivery',
        ]
        read_only_fields = ['id', 'last_login', 'date_joined']
        extra_kwargs = {
            'password': {'write_only': True},  # Ensure password is write-only
        }

    def create(self, validated_data):
        # Hash the password before saving
        password = validated_data.pop('password', None)
        instance = super().create(validated_data)
        if password:
            instance.set_password(password)
            instance.save()
        return instance

    def update(self, instance, validated_data):
        # Handle password hashing during updates
        password = validated_data.pop('password', None)
        instance = super().update(instance, validated_data)
        if password:
            instance.set_password(password)
            instance.save()
        return instance
    
    def to_representation(self, instance):
        # Custom method to ensure the hashed password is included in the response
        representation = super().to_representation(instance)
        representation['password'] = instance.password  # Include hashed password in response
        return representation
    
    

class Feedback_dSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

class Contact_dSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class DeliveryPersonLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryPersonLocation
        fields = '__all__'
