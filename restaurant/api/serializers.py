from rest_framework import serializers
from restaurant.models import Restaurant,Payment,Product,Cart,restaurantUser,foodItems


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = restaurantUser
        fields = '__all__'

class foodItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = foodItems
        fields = '__all__'

class RestaurantUserSerializer(serializers.ModelSerializer):
    
    food_items = serializers.SerializerMethodField()
    class Meta:
        model = restaurantUser
        fields = '__all__'

    def get_food_items(self, obj):
        items = obj.food_items.all()
        summary = f"{len(items)} items"
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