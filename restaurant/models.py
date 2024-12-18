from django.db import models
from django.forms import ValidationError
from django.core.validators import MinValueValidator , MaxValueValidator
# Create your models here.
from django.db import models
from customer.models import CustomUser  # Import CustomUser from the user app
from phonenumber_field.modelfields import PhoneNumberField
from customer.models import State,City,Place    

class restaurantUser(CustomUser):
    restaurantName = models.CharField(max_length=50)
    address = models.TextField()
    restaurantContact = PhoneNumberField()
    state = models.ForeignKey(State, on_delete=models.CASCADE, default=1)  # Ensure State with id=1 exists
    city = models.ForeignKey(City, on_delete=models.CASCADE, default=1)    # Ensure City with id=1 exists
    place = models.ForeignKey(Place, on_delete=models.CASCADE, default=1)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

class foodItems(models.Model):
    name = models.CharField(max_length=255) # Name of the food item
    price = models.DecimalField(max_digits=10, decimal_places=2) # Price of the food item
    image = models.ImageField(upload_to='images/') # Image of the food item
    category = models.CharField(max_length=255,default="None")  # Category of the food item
    restaurantName = models.ForeignKey(restaurantUser, related_name='food_items', on_delete=models.CASCADE)

# class State(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# class City(models.Model):
#     name = models.CharField(max_length=100)
#     state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='cities')

#     def __str__(self):
#         return self.name

# class Place(models.Model):
#     name = models.CharField(max_length=100)
#     city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='places')

#     def __str__(self):
#         return self.name

# class UserLocation(models.Model):
#     user_name = models.CharField(max_length=100)
#     state = models.ForeignKey(State, on_delete=models.CASCADE)
#     city = models.ForeignKey(City, on_delete=models.CASCADE)
#     place = models.ForeignKey(Place, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.user_name} - {self.place.name}, {self.city.name}, {self.state.name}"

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