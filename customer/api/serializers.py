from rest_framework import serializers
from customer.models import *

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
    state = serializers.CharField(source='state.name', read_only=True) 
    place = serializers.CharField(source='place.name', read_only=True)
    city = serializers.CharField(source='city.name', read_only=True) 
    
    class Meta: 
        model = customerUser 
        fields = '__all__'


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





