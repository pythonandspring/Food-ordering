from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from restaurant.models import Restaurant,Cart,Product,Payment,restaurantUser, foodItems
from .serializers import  *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser


# A viewset for viewing and editing restaurant instances.
class RestaurantViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    parser_classes = [MultiPartParser, FormParser]


# A viewset for viewing and editing restaurant user instances.
class RestaurantUserViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = restaurantUser.objects.all()
    serializer_class = RestaurantUserSerializer
    parser_classes = [MultiPartParser, FormParser]


# A viewset for viewing and editing food items instances.
class FoodItemsViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = foodItems.objects.all()
    serializer_class = foodItemsSerializer
    parser_classes = [MultiPartParser, FormParser]

# A viewset for viewing and editing product instances.
class ProductViewSet(viewsets.ModelViewSet):    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# A viewset for viewing and editing cart instances.
class CartViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

# A viewset for viewing and editing payment instances.    
class PaymentViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
