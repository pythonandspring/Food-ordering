"""
URL configuration for school project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from customer import views as customerviews
from restaurant import views as restaurantviews
from menu import views as menuviews
from order import views as orderviews
from delivery import views as deliveryviews
from . import views

urlpatterns = [

    

    path('admin/', admin.site.urls),

    path('', include('customer.urls')),
    # path('login/',customerviews.loginUser,name = 'login'),
    # path('logout/',customerviews.logoutUser,name = 'logout'),
    # path('feedback/', customerviews.feedback_form, name='feedback_form'),
    # path('contact/', customerviews.index, name='index'),
    # path('', customerviews.Home, name='Home'),
    # path('register/',customerviews.registerUser,name = 'register'),
    # path('forgetPassword/',customerviews.forgetPassword,name = 'forgetPassword'),

    path('', include('restaurant.urls')),
    # path('logoutRestaurant/',restaurantviews.logoutRestaurant,name = 'logoutR'),
    # path('loginRestaurant/',restaurantviews.loginRestaurant,name = 'loginRestaurant'),
    # path('registerRestaurant/',restaurantviews.registerRestaurant,name = 'registerRestaurant'),
    # path('addMenu/', restaurantviews.addMenu, name='addMenu'),
    
    path('loginDelivery/',deliveryviews.loginDelivery,name = 'loginDelivery'),
    path('registerDelivery/',deliveryviews.registerDelivery,name = 'registerDelivery'),
    path('home/', deliveryviews.home, name='home'),

    path('menu/',menuviews.menu,name = 'menu'),
    path('restaurantPage/', menuviews.restaurantPage, name='restaurantPage'),
    
    path('cart/', orderviews.Cart, name='cart'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

