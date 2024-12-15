from django.urls import path
from . import views

urlpatterns = [
    path('my-delivery-orders/', views.my_delivery_orders, name='my_delivery_orders'),
    path('update-status/', views.update_status, name='update_status'),
]
