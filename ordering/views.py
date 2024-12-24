from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from restaurant.models import foodItems
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from restaurant.models import foodItems, restaurantUser
from django.db.models import Q
from django.http import request
from customer.models import City
from django.http import request, JsonResponse
import speech_recognition as sr
from django.http import request, HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from .models import Feedback

def home(request):
    user = request.user
    if user.is_authenticated:
        if hasattr(user, 'customeruser'):
            return redirect('login')
        elif hasattr(user, 'restaurantuser'):
            return redirect('loginRestaurant')
        elif hasattr(user, 'deliveryuser'):
            return redirect('home')
    return render(request, 'home.html')



@login_required
def Cart(request):
    if 'cart' not in request.session:
        request.session['cart'] = {}
    
    cart = request.session['cart']
    cartDetails = {}
    totalCost = 0
    
    if request.method == 'POST':
        action = request.POST.get('action')
        item_id = request.POST.get('item_id')

        if action == 'add':
            if item_id in cart:
                cart[item_id] += 1
            else:
                cart[item_id] = 1
        elif action == 'remove':
            if item_id in cart:
                del cart[item_id]
        elif action == 'increment':
            if item_id in cart:
                cart[item_id] += 1
        elif action == 'decrement':
            if item_id in cart and cart[item_id] > 1:
                cart[item_id] -= 1

        request.session['cart'] = cart
        return redirect('cart')  # Redirect to the cart page to reflect changes
    
    for item_id, quantity in cart.items():
        item = foodItems.objects.get(id=item_id)
        totalCost += quantity * item.price
        cartDetails[item_id] = {"item": item, "quantity": quantity}

    return render(request, 'home/cart.html', {'cart': cartDetails, "totalCost": totalCost})




User = get_user_model()

@login_required
def menu(request):
    cities = City.objects.all()
    selected_city = request.GET.get('city')
    if selected_city:
        restaurant_list = restaurantUser.objects.filter(city_id=selected_city)
    else:
        restaurant_list = restaurantUser.objects.all()
    cities = City.objects.all()
    user = request.user
    query = request.GET.get('q')
    foods = foodItems.objects.all()
    
    if query:
        foods = foods.filter(Q(name__icontains=query))
    
    cartEmpty = True
    if hasattr(user, 'customeruser'):
        name = user.customeruser.name
    else:
        name = "No name found"

    if 'cart' not in request.session:
        request.session['cart'] = {}

    if request.method == 'POST':
        id = request.POST.get("id")
        cart = request.session.get('cart', {})
        if id in cart:
            cart[id] += 1
            cartEmpty = False
        else:
            cart[id] = 1
            cartEmpty = False
        request.session['cart'] = cart

    list_restaurant = restaurantUser.objects.all()

    return render(request, 'home/index1.html', {
        'name': name,
        'foodItems': foods,
        'cart': request.session.get('cart', {}),
        'Empty': cartEmpty,
        'restaurant_list': restaurant_list,
        'cities': cities
    })


@login_required
def restaurant_menu(request, restaurant_id):
    menu(request)
    restaurant = get_object_or_404(restaurantUser, id=restaurant_id)
    food_items = foodItems.objects.filter(restaurantName=restaurant)
    return render(request, 'home/restaurant_menu.html', {
        'restaurant': restaurant,
        'food_items': food_items
    })


def restaurantPage(request):
    rname = request.POST
    print(rname)

    return render(request,'restaurantPage.html')



from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
# from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'home/password_reset.html'  # Corrected template path
    email_template_name = 'home/password_reset_email.html'  # Corrected template path
    subject_template_name = 'home/password_reset_subject.txt'  # Corrected template path
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('Home')  # Corrected URL pattern
    
def run_speech_recog(request):
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)
            transcript = recognizer.recognize_google(audio)
            return JsonResponse({"transcript": transcript})
    except sr.UnknownValueError:
        return JsonResponse({"error": "Speech not recognized. Please try again."}, status=400)
    except sr.RequestError as e:
        return JsonResponse({"error": f"Speech recognition service error: {e}"}, status=500)
    except AttributeError as e:
        return JsonResponse({"error": "PyAudio is not installed or configured properly."}, status=500)



class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'home/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('Home')  # Corrected URL pattern

def forget_password(request):
    if request.method == 'POST':
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "authentication/password_reset_email.txt"
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
    return render(request=request, template_name="authentication/forgetPassword.html", context={"password_reset_form": password_reset_form})


@login_required
def feedback_form(request):
    if request.method == 'POST':
        stars = request.POST.get('stars')
        comments = request.POST.get('comment')
        user_type = 'customer' if request.user.is_user else 'restaurant' if request.user.is_restaurant else 'delivery'
        try:
            Fb = Feedback()
            Fb.stars = stars
            Fb.comments = comments
            Fb.user_type = user_type
            Fb.save()
            return render(request, 'thank_you.html')  # Render the thank you page
        except:
            return HttpResponse('<h1>Sorry!</h1><p>There is an issue</p>')
    return render(request, 'feedback.html')
