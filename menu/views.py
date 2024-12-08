from django.shortcuts import render,get_list_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from restaurant.models import foodItems, restaurantUser
from django.db.models import Q
from django.http import request

from .models import Menu
from restaurant.models import Restaurant
from .forms import MenuForm


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

    return render(request, 'index1.html', {
        'name': name,
        'foodItems': foods,
        'cart': request.session.get('cart', {}),
        'Empty': cartEmpty,
        'restaurant_list': list_restaurant
    })




def restaurantPage(request):
    rname = request.POST
    print(rname)

    return render(request,'restaurantPage.html')



def menu_list(request):
    menus = Menu.objects.all()
    return render(request, 'menu/menu_list.html', {'menus': menus})



def menu_detail(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    return render(request, 'menu/menu_detail.html', {'menu': menu})


def add_menu(request):
    if request.method == "POST":
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = MenuForm()
    return render(request, 'menu/menu_form.html', {'form': form})


def edit_menu(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    if request.method == "POST":
        form = MenuForm(request.POST, request.FILES, instance=menu)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = MenuForm(instance=menu)
    return render(request, 'menu/menu_form.html', {'form': form})


def delete_menu(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    if request.method == "POST":
        menu.delete()
        return redirect('menu_list')
    return render(request, 'menu/menu_confirm_delete.html', {'menu': menu})


# List menus for a specific restaurant
def restaurant_menus(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    menus = restaurant.menus.all()  
    return render(request, 'menu/restaurant_menus.html', {'restaurant': restaurant, 'menus': menus})