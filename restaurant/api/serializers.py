from rest_framework import serializers
from restaurant.models import restaurantUser,Payment,Product,Cart


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = restaurantUser
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'