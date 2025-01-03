from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('loginDelivery/', views.loginDelivery, name='loginDelivery'),
    path('registerDelivery/', views.registerDelivery, name='registerDelivery'),
    path('track_delivery/<int:order_id>/', views.track_delivery, name='track_delivery'),
    path('fetch_live_location/', views.fetch_live_location, name='fetch_live_location'),  # Updated line
    path('feedback_form/', views.feedback_form, name='feedback_form'),
]
