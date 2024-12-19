import re
from django.db import models
from django.forms import ValidationError
from django.contrib.auth.models import AbstractUser
from django.db import models

class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='cities')

    def __str__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='places')

    def __str__(self):
        return self.name
    
class CustomUser(AbstractUser):
    is_user = models.BooleanField(default=False)
    is_restaurant = models.BooleanField(default=False)
    is_delivery = models.BooleanField(default=False)

class customerUser(CustomUser):
    name = models.CharField(max_length=50)
    state = models.ForeignKey(State, on_delete=models.CASCADE, default=1)  # Ensure State with id=1 exists
    city = models.ForeignKey(City, on_delete=models.CASCADE, default=1)    # Ensure City with id=1 exists
    place = models.ForeignKey(Place, on_delete=models.CASCADE, default=1)  # Ensure Place with id=1 exists
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    address = models.CharField(max_length=255)  # Ensure address field is correctly defined
    customer = models.OneToOneField('Customer', on_delete=models.CASCADE, null=True, blank=True)  # Add OneToOneField to Customer

    def __str__(self):
        return f"{self.name} - {self.place.name}, {self.city.name}, {self.state.name}"
    
class Feedback(models.Model):
    stars = models.IntegerField()
    comments = models.TextField()

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.TextField()

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=255, default=1)  # Add password field

    def __str__(self):
        return self.name
    
    def clean(self):
        # Validate phone number
        if not re.match(r'^\d{10,15}$', self.phone_number):
            raise ValidationError('Phone number must be between 10 and 15 digits.')
    
    def view_menu(self):
        pass

    def make_payment(self):
        pass

    def add_to_cart(self):
        pass

    def delete_from_cart(self):
        pass

class Order(models.Model):
    customer = models.ForeignKey(customerUser, on_delete=models.CASCADE, related_name='orders')
    item = models.CharField(max_length=100)
    quantity = models.IntegerField()
    category = models.CharField(max_length=100)
    sum_of_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_no = models.CharField(max_length=20, unique=True)
    status = models.CharField(max_length=20, choices=[
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('OUT_FOR_DELIVERY', 'Out for Delivery'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled')
    ], default='PENDING')
    delivery_person = models.CharField(max_length=100, null=True, blank=True)
    delivery_contact = models.CharField(max_length=20, null=True, blank=True)  # Add delivery contact field
    restaurant_name = models.CharField(max_length=100)
    comments = models.TextField(null=True, blank=True)
    date_time = models.DateTimeField(auto_now_add=True)

    @property
    def get_status_choices(self):
        return self._meta.get_field('status').choices

    @staticmethod
    def get_orders_for_restaurant(restaurant_name):
        return Order.objects.filter(restaurant_name=restaurant_name)

    @staticmethod
    def get_orders_for_delivery_person(delivery_person_name):
        return Order.objects.filter(delivery_person=delivery_person_name)

    def __str__(self):
        return f"Order {self.order_no} - {self.customer.name}"
