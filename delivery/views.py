from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout, get_user_model
from delivery.models import deliveryUser
from restaurant.models import Cart

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
        elif user.is_delivery == False:
            messages.error(request, 'You are Registered as customer')
            return redirect('loginDelivery')
        elif user.is_restaurant == True:
            messages.error(request, 'You are Registered as restaurant')
            return redirect('loginDelivery')
        # Log the user in
        login(request, user)
        return redirect('home')  # Redirect to a homepage or dashboard after login

    return render(request, 'loginDelivery.html')

def registerDelivery(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        delivery_data = deliveryUser(
            username=email,
            password=make_password(password),
            email=email,
            deliveryContact=phone,
            name=name,
            address=address,
            is_delivery=True
        )

        # Check if the user already exists
        if deliveryUser.objects.filter(username=email).exists() and deliveryUser.objects.filter(is_delivery=True):
            messages.error(request, 'User Already Exist in the System')
            return redirect('registerDelivery')
        elif deliveryUser.objects.filter(username=email).exists() and deliveryUser.objects.filter(is_delivery=False):
            messages.error(request, 'You have Customer Account Using This Email ID. Try Another Email ID')
            return redirect('loginDelivery')
        else:
            delivery_data.save()
            messages.success(request, "Successfully Registered")
            return redirect('loginDelivery')
    return render(request, 'registerDelivery.html')

def my_delivery_orders(request):
    delivery_person = request.user  # Assuming logged-in delivery person
    orders = Cart.objects.filter(assigned_to=delivery_person)
    return render(request, 'my_delivery_orders.html', {'orders': orders})

def update_status(request):
    if request.method == "POST":
        order_id = request.POST.get('order_id')
        status = request.POST.get('status')
        delivery_date = request.POST.get('delivery_date')
        delivery_time = request.POST.get('delivery_time')
        
        try:
            order = Cart.objects.get(id=order_id)
            order.status = status
            order.delivery_date = delivery_date
            order.delivery_time = delivery_time
            order.save()
            return redirect('my_delivery_orders')
        except Cart.DoesNotExist:
            return HttpResponse("Order not found", status=404)
