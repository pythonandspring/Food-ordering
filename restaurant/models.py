from django.db import models
from django.forms import ValidationError
from django.core.validators import MinValueValidator , MaxValueValidator
# Create your models here.
from django.db import models
from customer.models import CustomUser  # Import CustomUser from the user app
from phonenumber_field.modelfields import PhoneNumberField

class restaurantUser(CustomUser):
    restaurantName = models.CharField(max_length=50)
    address = models.TextField()
    restaurantContact = PhoneNumberField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

class foodItems(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    category = models.CharField(max_length=255,default="None")  # Add this line
    restaurantName = models.ForeignKey(restaurantUser, related_name='food_items', on_delete=models.CASCADE)


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, default="Unknown Address")
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

class Cart(models.Model):
    number_of_products = models.IntegerField()
    product1 = models.CharField(max_length=100, null=True, blank=True)
    product2 = models.CharField(max_length=100, null=True, blank=True)
    product3 = models.CharField(max_length=100, null=True, blank=True)
    price = models.FloatField()
    total = models.FloatField()

    def __str__(self):
        return str(self.id)

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)

class Payment(models.Model):
    customer_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    card_type = models.CharField(max_length=50)
    card_no = models.CharField(max_length=20)
    def __str__(self):
        return self.name

