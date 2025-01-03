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
  # Import deliveryUser model
from delivery.models import deliveryUser  # Import deliveryUser model
from django.core.mail import send_mail  # Add this import
import os  # Add this import
from django.utils.crypto import get_random_string  # Add this import
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import BadHeaderError
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView, PasswordChangeView, PasswordResetCompleteView
from django.contrib.messages.views import SuccessMessageMixin
from geopy.geocoders import Nominatim
# Create your views here.

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
            login(request,user)
            messages.success(request,'Successfully Login')
            from_email = 'InFOODSys@gmail.com'  # Use the correct from_email
            user_name = restaurantUser.objects.get(email=username).restaurantName
            view_orders_link = request.build_absolute_uri('/restaurantOrders/')
            check_menu_link = request.build_absolute_uri('/addMenu/')
            send_mail(
    'Welcome Back, {}! Let’s Make Today Delicious!'.format(user_name),  # Subject line with dynamic user_name
    """Hello {},

Your kitchen is ready to serve! 🌟
Check out today’s orders and get ready to satisfy your customer's cravings!

👉 [View New Orders]({view_orders_link})
👉 [Check Your Menu]({check_menu_link})

We’re excited to see the magic your team creates today! 🍽️""".format(user_name, 
                                                                view_orders_link=view_orders_link, 
                                                                check_menu_link=check_menu_link),  # Plain text email content
    from_email,  # Sender's email
    [user.email],  # Recipient's email
    fail_silently=False,  # Fail silently if set to False
    html_message="""Hello {},<br><br>

Your kitchen is ready to serve! 🌟<br>
Check out today’s orders and get ready to satisfy your customer's cravings!<br><br>

👉 <a href="{view_orders_link}">View New Orders</a><br>
👉 <a href="{check_menu_link}">Check Your Menu</a><br>

We’re excited to see the magic your team creates today! 🍽️""".format(user_name, 
                                                                   view_orders_link=view_orders_link, 
                                                                   check_menu_link=check_menu_link)  # HTML email content
)
            render(request,'loginRestaurant.html')
            return redirect('addMenu')


    return render(request,'loginRestaurant.html')

    return render(request, 'loginRestaurant.html')

def registerRestaurant(request):
    states = State.objects.all()
    if request.method == 'POST':
        restaurantName = request.POST.get('restaurantName')
        address = request.POST.get('address')
        restaurantContact = request.POST.get('restaurantContact')
        email = request.POST.get('email')
        password = request.POST.get('password')
        state_id = request.POST.get('state')
        city_id = request.POST.get('city')
        place_id = request.POST.get('place')
        state = State.objects.get(id=state_id)
        city = City.objects.get(id=city_id)
        place = request.POST.get('place')

        geolocator = Nominatim(user_agent="RestaurantRegistration")
        location = geolocator.geocode(place)
        if not location:
            messages.error(request, 'Unable to fetch location details for the provided place.')
            return redirect('loginRestaurant')
        
        latitude = location.latitude
        longitude = location.longitude

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
            from_email = 'InFOODSys@gmail.com'  # Use the correct from_email
            user_name = restaurantUser.objects.get(email=email).restaurantName
            view_orders_link = request.build_absolute_uri('/restaurantOrders/')
            check_menu_link = request.build_absolute_uri('/addMenu/')
            send_mail(
    'Welcome, {}! Let’s Make Today Delicious!'.format(user_name),  # Subject line with dynamic user_name
    """Hello {},

Your kitchen is ready to serve! 🌟
Check out today’s orders and get ready to satisfy your customer's cravings!

👉 [View New Orders]({view_orders_link})
👉 [Check Your Menu]({check_menu_link})

We’re excited to see the magic your team creates today! 🍽️""".format(user_name, 
                                                                view_orders_link=view_orders_link, 
                                                                check_menu_link=check_menu_link),  # Plain text email content
    from_email,  # Sender's email
    [restaurant_data.email],  # Recipient's email
    fail_silently=False,  # Fail silently if set to False
    html_message="""Hello {},<br><br>

Your kitchen is ready to serve! 🌟<br>
Check out today’s orders and get ready to satisfy your customer's cravings!<br><br>

👉 <a href="{view_orders_link}">View New Orders</a><br>
👉 <a href="{check_menu_link}">Check Your Menu</a><br>

We’re excited to see the magic your team creates today! 🍽️""".format(user_name, 
                                                                   view_orders_link=view_orders_link, 
                                                                   check_menu_link=check_menu_link)  # HTML email content
)
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
def toggle_stock(request, food_id):
    food = foodItems.objects.get(id=food_id, restaurantName=request.user.restaurantuser)
    food.is_out_of_stock = not food.is_out_of_stock
    food.save()
    messages.success(request, f"Stock status of {food.name} updated successfully")
    return redirect('addMenu')

@login_required
def logoutRestaurant(request):
    user = get_user_model()
    logout(request)
    return redirect("logout")

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
    restaurant = restaurantUser.objects.get(email=request.user.email)
    delivery_persons = deliveryUser.objects.filter(is_delivery=True)
    return render(request, 'delivery.html', {
        'order': order,
        'restaurant': restaurant,
        'delivery_persons': delivery_persons
    })
@login_required
def update_delivery_person(request, order_id):
    if request.method == 'POST':
        order = Order.objects.get(id=order_id)
        delivery_person_id = request.POST.get('delivery_person')
        delivery_person = deliveryUser.objects.get(id=delivery_person_id)
        order.delivery_person = delivery_person.name
        order.save()
        messages.success(request, f"Delivery person {delivery_person.name} assigned to order {order.order_no}")
    return redirect('restaurant_orders')

@login_required
def delete_order(request, order_id):
    order = Order.objects.get(id=order_id)
    order.delete()
    messages.success(request, 'Order deleted successfully')
    return redirect('restaurant_orders')

User = get_user_model()

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'authentication/password_reset.html'  # Corrected template path
    email_template_name = 'authentication/password_reset_email.html'  # Corrected template path
    subject_template_name = 'authentication/password_reset_subject.txt'  # Corrected template path
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('loginRestaurant')  # Corrected URL pattern

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'authentication/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('loginRestaurant')  # Corrected URL pattern

class PasswordResetComplete(SuccessMessageMixin, PasswordResetCompleteView):
    template_name = 'authentication/password_reset_complete.html'
    success_message = "Your password has been set. You may go ahead and log in now."
    success_url = reverse_lazy('loginRestaurant')

def forget_password(request):
    if request.method == 'POST':
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested for Your Account"
                    email_template_name = "authentication/password_reset_email.html"
                    c = {
                        "email": user.email,
                        'domain': request.META['HTTP_HOST'],
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="authentication/password_reset.html", context={"password_reset_form": password_reset_form})
