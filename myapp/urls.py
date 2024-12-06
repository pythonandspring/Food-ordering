# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('delivery-registration/', views.delivery_registration, name='delivery_registration'),  # This links the root URL to the index view
    path('customer-registration/', views.customer_registration, name='customer_registration'),
    path('restaurant-registration/', views.restaurant_registration, name='restaurant_registration'),
    path('login/', views.login_view, name='login'),
    path('', views.homepage_view, name='homepage'),]
