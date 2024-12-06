from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model  # Import get_user_model instead of User

# Home view for logged-in users
@login_required
def home(request):
    return render(request, 'Deliveryhome.html')

def loginDelivery(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, 'Invalid Username or Password')
            return redirect('loginDelivery')

        # Log the user in
        login(request, user)
        return redirect('home')  # Redirect to a homepage or dashboard after login

    return render(request, 'loginDelivery.html')


def registerDelivery(request):
    if request.method == 'POST':
        # Get form data
        username = request.POST.get('email')
        password = request.POST.get('password')

        # Use the correct user model
        User = get_user_model()  # Get the custom user model

        # Check if the user already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'User already exists with this email address.')
            return redirect('registerDelivery')

        # Create a new user
        user = User.objects.create_user(username=username, password=password)
        messages.success(request, 'Successfully registered. Please log in.')
        return redirect('loginDelivery')

    return render(request, 'registerDelivery.html')
