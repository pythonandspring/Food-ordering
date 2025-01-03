from rest_framework import serializers
from customer.models import *
from django.contrib.auth.hashers import make_password


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class CustomerUserSerializer(serializers.ModelSerializer):
    place = serializers.CharField(required=False)
    customer = serializers.PrimaryKeyRelatedField(read_only=True)
    password = serializers.CharField(write_only=True)
    orders = serializers.SerializerMethodField(read_only=True)
   
    class Meta:
        model = customerUser
        fields = [
            'id', 'username', 'email', 'is_superuser', 'name', 'state', 'city', 'place', 
            'latitude', 'longitude', 'address', 'customer', 'orders' ,'password', 'is_staff', 
            'is_active', 'date_joined', 'last_login', 'is_user', 
            'is_restaurant', 'is_delivery',
        ]
        read_only_fields = ['id', 'last_login', 'date_joined', 'customer']
        extra_kwargs = {
            'password': {'write_only': True},  # Ensure password is write-only
        }

    def get_orders(self, obj):
        return obj.orders.count()
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        hashed_password = make_password(password)

        # Create a new Customer instance
        customer_data = {
            "name": validated_data.get("name", ""),
            "address": validated_data.get("address", ""),
            "email": validated_data.get("email", ""),
            "password": hashed_password,
        }
        customer = Customer.objects.create(**customer_data)

        # Add the created Customer to the customerUser instance
        validated_data['customer'] = customer
        validated_data['password'] = hashed_password
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Update customerUser instance
        password = validated_data.pop('password', None)

        customer = instance.customer

        # Update the related Customer instance
        if customer:
            customer.name = validated_data.get("name", customer.name)
            customer.address = validated_data.get("address", customer.address)
            #customer.phone_number = phone_number if phone_number else customer.phone_number
            customer.email = validated_data.get("email", customer.email)
            if password:
                customer.password = make_password(password) 
            customer.save()
        if password:
            validated_data['password'] = make_password(password)

        # Proceed with updating the customerUser instance
        return super().update(instance, validated_data)
    
    def to_representation(self, instance):
        # Custom method to ensure the hashed password is included in the response
        representation = super().to_representation(instance)
        representation['password'] = instance.password  # Include hashed password in response
        return representation
    
class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'





