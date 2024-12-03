from django.db import models
from menu.models import Menu
from delivery.models import deliveryUser
# Create your models here.
class Order(models.Model):
    item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    sum_of_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_no = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[('PENDING', 'Pending'), ('CONFIRMED', 'Confirmed'), ('OUT_FOR_DELIVERY', 'Out for Delivery'), ('DELIVERED', 'Delivered'), ('CANCELLED', 'Cancelled')], default='PENDING')
    delivery_person = models.ForeignKey(deliveryUser, on_delete=models.SET_NULL, null=True, blank=True)
    restaurant_name = models.CharField(max_length=100)
    comments = models.TextField(blank=True, null=True)
    date_time = models.DateTimeField(auto_now_add=True)