from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from restaurant.models import restaurantUser,foodItems
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout,get_user_model
from customer.models import Order
from delivery.models import deliveryUser 

# Import deliveryUser model
# Create your views here.


def loginRestaurant(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        
        # if not User.objects.filter(email = username).exists():
        #     messages.error(request,'Username is not in database')
        #     return redirect('login')

        user = authenticate(username=username, password=password)
   
        if user is None:
            messages.error(request,'Invalid Password or Username')
            return redirect('loginRestaurant')

        elif user.is_delivery==True:
            messages.error(request,'You are Registered as delivery')
            return redirect('loginRestaurant')

        elif user.is_restaurant==False:
            messages.error(request,'You are a User')
            return redirect('loginRestaurant')
        else:
            login(request,user)
            messages.success(request,'Successfully Login')
            render(request,'loginRestaurant.html')
            return redirect('addMenu')


    return render(request,'loginRestaurant.html')


def registerRestaurant(request):
    if request.method == 'POST':
        
        restaurantName = request.POST.get('restaurantName')
        address = request.POST.get('address')
        restaurantContact = request.POST.get('restaurantContact')
        email = request.POST.get('email')
        password = request.POST.get('password')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        
        restaurant_data = restaurantUser(
            restaurantName=restaurantName,
            address=address,
            restaurantContact=restaurantContact,
            email=email,
            username=email,
            is_restaurant=True,
            password=make_password(password),
            latitude=latitude,
            longitude=longitude
        )
        
        if restaurantUser.objects.filter(email=email).exists() and restaurantUser.objects.filter(is_restaurant=True):
            messages.error(request,'User Already Exist in the System')
            return redirect('loginRestaurant')
        
        elif restaurantUser.objects.filter(email=email).exists() and restaurantUser.objects.filter(is_restaurant=False):
            messages.error(request,'You have Customer Account Using This Email ID. Try Another Email ID')
            return redirect('loginRestaurant')

        else:
            restaurant_data.save()
            messages.success(request,"Successfully Registered")
            return redirect('loginRestaurant')

    return render(request,'registerRestaurant.html')

@login_required
def addMenu(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        category = request.POST.get('category')  # Add this line
        restaurant_user = request.user.restaurantuser
        food_item = foodItems(name=name, price=price, image=image, category=category, restaurantName=restaurant_user)  # Add 'category'
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
        food.category = request.POST.get('food-category')  # Add this line
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
    print(restaurant_name)
    orders = Order.get_orders_for_restaurant(restaurant_name)
    
    delivery_user = deliveryUser.objects.all()
    
    return render(request, 'restaurantorders.html', {
        'orders': orders,
        'deliver_user':delivery_user,
        'messages': messages.get_messages(request)})

@login_required
def update_order_status(request, order_id):
    if request.method == 'POST':
        order = Order.objects.get(id=order_id)
        order.status = request.POST.get('status')
        order.save()
        messages.success(request, f"Order status of {order.customer.name} is {order.get_status_display()}")
    return redirect('restaurant_orders')

# @login_required
# def assign_delivery_person(request, order_id):
#     order = Order.objects.get(id=order_id)
#     delivery_persons = deliveryUser.objects.all()
#     return render(request, 'delivery.html', {'order': order, 'delivery_persons': delivery_persons})

# @login_required
# def update_delivery_person(request, order_id):
#     if request.method == 'POST':
#         order = Order.objects.get(id=order_id)
#         delivery_person_id = request.POST.get('delivery_person')
#         delivery_person = deliveryUser.objects.get(id=delivery_person_id)
#         order.delivery_person = delivery_person.name
#         order.delivery_contact = delivery_person.deliveryContact  # Add delivery contact
#         order.save()
#         messages.success(request, f"Delivery person {delivery_person.name} assigned to order {order.order_no}")
#     return redirect('restaurant_orders')


@login_required
def assign_delivery_person(request, order_id):
    if request.method == 'POST':
        order = get_object_or_404(Order, id=order_id)
        delivery_person_id = request.POST.get('delivery_person')
        delivery_person = get_object_or_404(deliveryUser, id=delivery_person_id)
        order.delivery_person = delivery_person.name
        order.delivery_contact = delivery_person.deliveryContact  # Add delivery contact
        order.save()
        delivery_person.status = 'unavailable'  # Update delivery person's status
        delivery_person.save()
        messages.success(request, f"Delivery person {delivery_person.name} assigned to order {order.order_no}")
    return redirect('restaurant_orders')
