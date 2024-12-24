from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

from customer.models import customerUser, Contact, Order, Customer, State, City, Place
from restaurant.models import foodItems, restaurantUser
import os
from random import choice
from django.contrib.auth import get_user_model
# Create your views here.

User = get_user_model()

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, 'Invalid Password or Username')
            return redirect('login')
        elif user.is_delivery:
            messages.error(request, 'You are Registered as delivery')
            return redirect('login')
        elif user.is_restaurant:
            messages.error(request, 'You are Registered as restaurant')
            return redirect('login')
        else:
            login(request, user)
            messages.success(request, 'Successfully Login')
            from_email = 'InFOODSys@gmail.com'  # Use the correct from_email
            user_name = customerUser.objects.get(email=username).name
            restaurant_links = "<br>".join([f"<a href='{request.build_absolute_uri(f'/restaurant/{restaurant.id}/menu/')}'>{restaurant.restaurantName}</a>" for restaurant in restaurantUser.objects.all()])
            send_mail(
                'Welcome Back, {}'.format(user_name),
                """Hello {},<br><br>
                Craving something delicious? 🍔🌮<br>
                Explore your favorites or try something new today! 🚀<br>
                Browse Restaurants 👉 <br>
                {}<br><br>
                We're here to deliver happiness right to your doorstep. 🛵💨<br>
                Bon appétit,<br>
                Food Ordering Team 🍽️""".format(user_name, restaurant_links),
                from_email,
                [user.email],
                fail_silently=False,
                html_message="""Hello {},<br><br>
                Craving something delicious? 🍔🌮<br>
                Explore your favorites or try something new today! 🚀<br><br>
                Browse Restaurants 👉 <br>
                {}<br><br>
                We're here to deliver happiness right to your doorstep. 🛵💨<br>
                Bon appétit,<br>
                Food Ordering Team 🍽️""".format(user_name, restaurant_links)
            )
            render(request,'authentication/login.html')
            return redirect('menu')

    return render(request, 'authentication/login.html')

def registerUser(request):
    states = State.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        state_id = request.POST.get('state')
        city_id = request.POST.get('city')
        place_id = request.POST.get('place')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        password = request.POST.get('password')

        state = State.objects.get(id=state_id)
        city = City.objects.get(id=city_id)
        place = Place.objects.get(id=place_id)

        if customerUser.objects.filter(email=email).exists():
            messages.error(request, 'User Already Exists in the System')
            return redirect('registerUser')

        hashed_password = make_password(password)

        try:
            customer = Customer.objects.create(
                name=name,
                address=address,
                phone_number=phone,
                email=email,
                password=hashed_password
            )

            user = customerUser.objects.create(
                name=name,
                email=email,
                username=email,
                password=hashed_password,
                is_user=True,
                state=state,
                city=city,
                place=place,
                address=address,
                latitude=latitude,
                longitude=longitude,
                customer=customer
            )
            user.save()
            messages.success(request, 'Successfully Registered')
            return redirect('login')
        except Exception as e:
            messages.error(request, f'Error!! Try Again: {e}')
            return redirect('registerUser')

    return render(request, 'authentication/register.html', {'states': states})

def forgetPassword(request):
    return render(request, 'authentication/forgetPassword.html')

def logoutUser(request):
    logout(request)
    return render(request, 'authentication/logout.html')

def feedback_form(request):
    pass

def index(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.save()
        return render(request, 'thank_you.html')  # Render the thank you page
    return render(request, 'contact.html')

def Home(request):
    return render(request, 'home.html')

def load_cities(request):
    state_id = request.GET.get('state_id')
    cities = City.objects.filter(state_id=state_id).values('id', 'name')
    return JsonResponse(list(cities), safe=False)

def load_places(request):
    city_id = request.GET.get('city_id')
    places = Place.objects.filter(city_id=city_id).values('id', 'name')
    return JsonResponse(list(places), safe=False)

def orders(request):
    user_orders = Order.objects.filter(customer=request.user)
    return render(request, 'home/orders.html', {'orders': user_orders})

@login_required
def make_payment(request):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        print(cart)
        orders = {}
        for item_id, item in cart.items():
            food_item = foodItems.objects.get(id=item_id)
            restaurant_name = food_item.restaurantName.restaurantName
            if restaurant_name not in orders:
                orders[restaurant_name] = {
                    'items': [],
                    'total_price': 0,
                    'restaurant_name': restaurant_name
                }
            orders[restaurant_name]['items'].append({
                'name': food_item.name,
                'quantity': item,
                'category': food_item.category,
                'price': food_item.price * item
            })
            orders[restaurant_name]['total_price'] += food_item.price * item

        order_instance = None
        for order in orders.values():
            order_instance = Order.objects.create(
                customer=customerUser.objects.get(id=request.user.id),
                item=', '.join([f"{i['name']} (x{i['quantity']})" for i in order['items']]),
                quantity=sum([i['quantity'] for i in order['items']]),
                category=', '.join(set([i['category'] for i in order['items']])),
                sum_of_price=order['total_price'],
                order_no=get_random_string(10),
                restaurant_name=order['restaurant_name']
            )
            order_instance.save()

        request.session['cart'] = {}
        if order_instance:
            return redirect('track_locations', order_id=order_instance.id)
        else:
            messages.error(request, "No orders were created.")
            return redirect('orders')
    return redirect('cart')

@login_required
def track_locations(request, order_id):
    order = get_object_or_404(Order, id=order_id, customer=request.user)
    customer = order.customer
    try:
        restaurant = restaurantUser.objects.get(restaurantName=order.restaurant_name)
    except restaurantUser.DoesNotExist:
        messages.error(request, "Restaurant user does not exist.")
        return redirect('orders')

    context = {
        'order': order,
        'customer_latitude': customer.latitude,
        'customer_longitude': customer.longitude,
        'restaurant_latitude': restaurant.latitude,
        'restaurant_longitude': restaurant.longitude
    }

    return render(request, 'home/track_locations.html', context)

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        state_id = request.POST['state']
        city_id = request.POST['city']
        place_id = request.POST['place']
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']
        password = request.POST['password']

        state = State.objects.get(id=state_id)
        city = City.objects.get(id=city_id)
        place = Place.objects.get(id=place_id)

        customer_user = customerUser.objects.create(
            name=name,
            email=email,
            state=state,
            city=city,
            place=place,
            address = address,
            latitude=latitude,
            longitude=longitude,
        )
        customer_user.set_password(password)
        customer_user.save()

        messages.success(request, 'Registration Successful!')
        return redirect('register')

    states = State.objects.all()
    return render(request, 'authentication/register.html', {'states': states})
