from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from restaurant.models import restaurantUser, foodItems
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout, get_user_model
from customer.models import Order
from delivery.models import deliveryUser
from customer.models import State,City,Place
# from restaurant.models import State, City, Place, UserLocation

# Create your views here.

def loginRestaurant(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, 'Invalid Password or Username')
            return redirect('loginRestaurant')

        elif user.is_delivery:
            messages.error(request, 'You are Registered as delivery')
            return redirect('loginRestaurant')

        elif not user.is_restaurant:
            messages.error(request, 'You are a User')
            return redirect('loginRestaurant')
        else:
            login(request, user)
            messages.success(request, 'Successfully Login')
            return redirect('addMenu')  # Ensure proper redirection after login

    return render(request, 'loginRestaurant.html')

def registerRestaurant(request):
    states = State.objects.all()
    if request.method == 'POST':
        restaurantName = request.POST.get('restaurantName')
        address = request.POST.get('address')
        restaurantContact = request.POST.get('restaurantContact')
        email = request.POST.get('email')
        password = request.POST.get('password')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        state_id = request.POST.get('state')
        city_id = request.POST.get('city')
        place_id = request.POST.get('place')
        state = State.objects.get(id=state_id)
        city = City.objects.get(id=city_id)
        place = Place.objects.get(id=place_id)

        restaurant_data = restaurantUser(
            restaurantName=restaurantName,
            address=address,
            restaurantContact=restaurantContact,
            state=state, 
            city=city, 
            place=place,
            email=email,
            username=email,
            is_restaurant=True,
            password=make_password(password),
            latitude=latitude,
            longitude=longitude
        )

        if restaurantUser.objects.filter(email=email).exists() and restaurantUser.objects.filter(is_restaurant=True):
            messages.error(request, 'User Already Exist in the System')
            return redirect('loginRestaurant')

        elif restaurantUser.objects.filter(email=email).exists() and restaurantUser.objects.filter(is_restaurant=False):
            messages.error(request, 'You have Customer Account Using This Email ID. Try Another Email ID')
            return redirect('loginRestaurant')

        else:
            restaurant_data.save()
            messages.success(request, "Successfully Registered")
            return redirect('loginRestaurant')

    return render(request, 'registerRestaurant.html', {'states': states})

@login_required
def addMenu(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        category = request.POST.get('category')
        restaurant_user = request.user.restaurantuser
        food_item = foodItems(name=name, price=price, image=image, category=category, restaurantName=restaurant_user)
        food_item.save()
        messages.success(request, 'Food item added successfully')

    food_items = foodItems.objects.filter(restaurantName=request.user.restaurantuser)
    return render(request, 'addMenu.html', {'food_items': food_items})

@login_required
def update_food(request, food_id):
    food = foodItems.objects.get(id=food_id, restaurantName=request.user.restaurantuser)
    if request.method == 'POST':
        food.name = request.POST.get('food-title')
        food.price = request.POST.get('food-price')
        food.category = request.POST.get('food-category')
        if request.FILES.get('food-image'):
            food.image = request.FILES.get('food-image')
        food.save()
        messages.success(request, 'Food item updated successfully')
        return redirect('addMenu')
    return render(request, 'update.html', {'food': food})

@login_required
def delete_food(request, food_id):
    food = foodItems.objects.get(id=food_id, restaurantName=request.user.restaurantuser)
    food.delete()
    messages.success(request, 'Food item deleted successfully')
    return redirect('addMenu')

@login_required
def logoutRestaurant(request):
    user = get_user_model()
    logout(request)
    return redirect("feedback_form")

@login_required
def restaurant_orders(request):
    restaurant_user = restaurantUser.objects.get(email=request.user.email)
    restaurant_name = restaurant_user.restaurantName
    orders = Order.objects.filter(restaurant_name=restaurant_name)
    return render(request, 'restaurantorders.html', {'orders': orders, 'messages': messages.get_messages(request)})

@login_required
def update_order_status(request, order_id):
    if request.method == 'POST':
        order = Order.objects.get(id=order_id)
        order.status = request.POST.get('status')
        order.save()
        messages.success(request, f"Order status of {order.customer.name} is {order.get_status_display()}")
    return redirect('restaurant_orders')

@login_required
def assign_delivery_person(request, order_id):
    order = Order.objects.get(id=order_id)
    delivery_persons = deliveryUser.objects.filter(is_delivery=True)
    return render(request, 'delivery.html', {'order': order, 'delivery_persons': delivery_persons})

@login_required
def update_delivery_person(request, order_id):
    if request.method == 'POST':
        order = Order.objects.get(id=order_id)
        delivery_person_id = request.POST.get('delivery_person')
        delivery_person = deliveryUser.objects.get(id=delivery_person_id)
        order.delivery_person = delivery_person.name
        order.delivery_contact = delivery_person.deliveryContact
        order.save()
        messages.success(request, f"Delivery person {delivery_person.name} assigned to order {order.order_no}")
    return redirect('restaurant_orders')

@login_required
def delete_order(request, order_id):
    order = Order.objects.get(id=order_id)
    order.delete()
    messages.success(request, 'Order deleted successfully')
    return redirect('restaurant_orders')
# def location_view(request):
#     states = State.objects.all()
#     if request.method == 'POST':
#         user_name = request.POST.get('user_name')
#         state_id = request.POST.get('state')
#         city_id = request.POST.get('city')
#         place_id = request.POST.get('place')

#         state = State.objects.get(id=state_id)
#         city = City.objects.get(id=city_id)
#         place = Place.objects.get(id=place_id)

#         UserLocation.objects.create(user_name=user_name, state=state, city=city, place=place)
#         return redirect('location')

#     return render(request, 'new_app/location.html', {'states': states})

# def load_cities(request):
#     state_id = request.GET.get('state_id')
#     cities = City.objects.filter(state_id=state_id).values('id', 'name')
#     return JsonResponse(list(cities), safe=False)

# def load_places(request):
#     city_id = request.GET.get('city_id')
#     places = Place.objects.filter(city_id=city_id).values('id', 'name')
#     return JsonResponse(list(places), safe=False)
