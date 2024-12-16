from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout, get_user_model
from delivery.models import deliveryUser
from customer.models import Order


# Home view for logged-in users
@login_required
def home(request):
    delivery_user = request.user
    assigned_orders = Order.objects.filter(delivery_person = delivery_user)
    return render(request, 'Deliveryhome.html', {'assigned_orders': assigned_orders})

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



#view to change driver's status when an order is assigned 

# from django.shortcuts import get_object_or_404, redirect
# from django.http import HttpResponse
# from delivery.models import deliveryUser
# from .models import Order

# def assign_delivery_driver(order_id):
#     order = get_object_or_404(Order, id=order_id)
#     available_drivers = deliveryUser.objects.filter(status='available')

#     if available_drivers.exists():
#         driver = available_drivers.first()  # Assign the first available driver
#         order.delivery_person = driver
#         order.save()
#         driver.status = 'unavailable'  # Mark the driver as unavailable
#         driver.save()
#         return redirect('order_detail', order_id=order.id)  # Redirect to the order detail page
#     else:
#         return HttpResponse("No available delivery drivers", status=404)