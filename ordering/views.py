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

def home(request):
    return render(request, 'home/home.html')



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
        'restaurant_list': list_restaurant
    
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