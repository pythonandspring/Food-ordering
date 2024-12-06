from django.shortcuts import render

# Create your views here.
# myapp/views.py



def index(request):
    return render(request, 'home/Delivery_reg.html')

def login_view(request):
    return render(request, 'home/login.html')  # Ensure 'login.html' exists in your templates folder


def homepage_view(request):
    return render(request, 'home/HomePage.html')

def delivery_registration(request):
    return render(request, 'home/delivery_registration.html') 

def customer_registration(request):
    return render(request, 'home/customer_registration.html') 

def restaurant_registration(request):
    return render(request, 'home/restaurant_registration.html')  # Adjust for your app and folder structure

from django.shortcuts import redirect
from django.contrib.auth import authenticate, login



