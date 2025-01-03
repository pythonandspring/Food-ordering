from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from customer.models import customerUser,Contact,Place,City,State,Order,Customer
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import MultiPartParser, FormParser


# A viewset for viewing and editing customer user instances.  
class CustomerViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    parser_classes = [MultiPartParser, FormParser]  

    
# A viewset for viewing and editing contact instances.  
class ContactViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    parser_classes = [MultiPartParser, FormParser]

# A viewset for viewing and editing customer user instances.  
class CustomerUserViewSet(viewsets.ModelViewSet):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = customerUser.objects.all() 
    serializer_class = CustomerUserSerializer
    parser_classes = [MultiPartParser, FormParser]

# A viewset for viewing and editing state instances.
class StateViewSet(viewsets.ModelViewSet): 
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = State.objects.all() 
    serializer_class = StateSerializer
    parser_classes = [MultiPartParser, FormParser]

# A viewset for viewing and editing place instances.
class PlaceViewSet(viewsets.ModelViewSet): 
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Place.objects.all() 
    serializer_class = PlaceSerializer
    parser_classes = [MultiPartParser, FormParser]

# A viewset for viewing and editing city instances.
class CityViewSet(viewsets.ModelViewSet): 
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = City.objects.all() 
    serializer_class = CitySerializer
    parser_classes = [MultiPartParser, FormParser]

# A viewset for viewing and editing order instances.
class OrderViewSet(viewsets.ModelViewSet):
    authenticatio_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    parser_classes = [MultiPartParser, FormParser]
