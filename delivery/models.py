from django.db import models
from datetime import date, timedelta
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from customer.models import CustomUser
from phonenumber_field.modelfields import PhoneNumberField
from customer.models import State, City, Place
class deliveryUser(CustomUser):
    name = models.CharField(max_length=50)
    address = models.TextField()
    state = models.ForeignKey(State, on_delete=models.CASCADE, default=1)  # Ensure State with id=1 exists
    city = models.ForeignKey(City, on_delete=models.CASCADE, default=1)    # Ensure City with id=1 exists
    place = models.ForeignKey(Place, on_delete=models.CASCADE, default=1)
    deliveryContact = PhoneNumberField(null=True, blank=True)

    def __str__(self):
        return self.name  # Use name for display

class Feedback(models.Model):
    stars = models.IntegerField()
    comments = models.TextField()

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.TextField()

    def __str__(self):
        return self.name

class DeliveryPerson(models.Model):
    DELIVERY_STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('on-duty', 'On Duty'),
        ('off-duty', 'Off Duty'),
        ('delivering', 'Delivering'),
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    vehicle_type = models.CharField(max_length=50, blank=True, null=True)
    license_number = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=10, choices=DELIVERY_STATUS_CHOICES, default='inactive')
    current_location = models.CharField(max_length=255, blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    available_for_delivery = models.BooleanField(default=True)
    bank_account_details = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    profile_picture_url = models.URLField(blank=True, null=True)
    emergency_contact_name = models.CharField(max_length=255, blank=True, null=True)
    emergency_contact_phone = models.CharField(max_length=20, blank=True, null=True)
    vehicle_registration_date = models.DateField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
