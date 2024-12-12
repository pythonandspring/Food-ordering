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
from delivery.models import deliveryUser
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
        elif user.is_delivery==False:
            messages.error(request,'You are Registered as customer')
            return redirect('loginDelivery')
        
        elif user.is_restaurant==True:
            messages.error(request,'You are Registered as restaurant')
            return redirect('loginDelivery')
        # Log the user in
        login(request, user)
        return redirect('home')  # Redirect to a homepage or dashboard after login

    return render(request, 'loginDelivery.html')


def registerDelivery(request):
    if request.method == 'POST':
        # Get form data
        email = request.POST.get('email')
        password = request.POST.get('password')

        deliveryContact = request.POST.get('deliveryContact')
        #deliveryEmail = request.POST.get('email')  # Assuming email is used as username as well

        delivery_data = deliveryUser(username=email,
                                    password=make_password(password),

                                    email=email,
                                    deliveryContact=deliveryContact,
                                    is_delivery=True)
        
        # Use the correct user model
        User = get_user_model()  # Get the custom user model

        # Check if the user already exists
        # if deliveryUser.objects.filter(username=username).exists():
        #     messages.error(request, 'User already exists with this email address.')
        #     return redirect('registerDelivery')
        if deliveryUser.objects.filter(username=email).exists() and deliveryUser.objects.filter(is_delivery=True):
            messages.error(request,'User Already Exist in the System')
            return redirect('registerDelivery')
        
        elif deliveryUser.objects.filter(username=email).exists() and deliveryUser.objects.filter(is_delivery=False):
            messages.error(request,'You have Customer Account Using This Email ID. Try Another Email ID')
            return redirect('loginDelivery')
        # Create a new user
        # user = User.objects.create_user(username=username, password=password)
        # messages.success(request, 'Successfully registered. Please log in.')
        # return redirect('loginDelivery')
        else:
            delivery_data.save()
            messages.success(request,"Successfully Registered")
            return redirect('loginDelivery')
    return render(request, 'registerDelivery.html')
