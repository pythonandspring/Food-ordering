from django.urls import path, include
from .api import urls as api_urls
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from restaurant import views as restaurantviews

urlpatterns = [
    path('logoutRestaurant/', restaurantviews.logoutRestaurant, name='logoutR'),
    path('loginRestaurant/', restaurantviews.loginRestaurant, name='loginRestaurant'),
    path('registerRestaurant/', restaurantviews.registerRestaurant, name='registerRestaurant'),
    path('addMenu/', restaurantviews.addMenu, name='addMenu'),
    path('update/<int:food_id>/', restaurantviews.update_food, name='update_food'),
    path('delete/<int:food_id>/', restaurantviews.delete_food, name='delete_food'),
    path('restaurantOrders/', restaurantviews.restaurant_orders, name='restaurant_orders'),
    path('updateOrderStatus/<int:order_id>/', restaurantviews.update_order_status, name='update_order_status'),
    path('assignDeliveryPerson/<int:order_id>/', restaurantviews.assign_delivery_person, name='assign_delivery_person'),
    path('updateDeliveryPerson/<int:order_id>/', restaurantviews.update_delivery_person, name='update_delivery_person'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
