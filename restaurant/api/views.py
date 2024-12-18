from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from restaurant.models import restaurantUser,Product,Payment, Cart
from restaurant.models import restaurantUser,Cart,Product,Payment
from .serializers import  RestaurantSerializer, CartSerializer,ProductSerializer, PaymentSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class RestaurantViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = restaurantUser.objects.all()
    serializer_class = RestaurantSerializer

class ProductViewSet(viewsets.ModelViewSet):    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CartViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    
class PaymentViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
