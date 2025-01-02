from rest_framework import serializers
from restaurant.models import Restaurant,Payment,Product,Cart,restaurantUser,foodItems
from customer.models import Place


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class foodItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = foodItems
        fields = [
            'id', 'name', 'price', 'image', 'category', 
            'restaurantName', 'is_out_of_stock'
        ]
        read_only_fields = ['id']  # 'id' is read-only

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price cannot be negative.")
        return value

class RestaurantUserSerializer(serializers.ModelSerializer):
    # Fields to be included in the serializer
    food_items = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True, required=True)  # For password handling in POST/PUT requests

    class Meta:
        model = restaurantUser
        fields = [
            'id', 'username', 'email', 'is_superuser',
            'restaurantName', 'food_items','address', 'is_restaurant', 'is_delivery',
            'is_staff', 'is_active', 'date_joined', 'last_login', 'is_user',
            'restaurantContact', 'state', 'city', 'place', 'latitude', 
            'longitude', 'password'
        ]
        read_only_fields = ['id', 'last_login', 'date_joined', 'is_superuser']
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

    # Method to count the menu items 
    def get_food_items(self, obj):
        items = obj.food_items.all()
        summary = f"{len(items)}"
        return summary
    
    

      
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
