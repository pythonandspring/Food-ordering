import re
from django.db import models
from django.forms import ValidationError
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_user = models.BooleanField(default=False)
    is_restaurant = models.BooleanField(default=False)


class customerUser(CustomUser):
    name = models.CharField(max_length=50)

    
class Feedback(models.Model):
    stars = models.IntegerField()
    comments = models.TextField()

class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    subject=models.TextField()
    def __str__(self):
        return self.name
    
class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=255,default=1)  # Add password field
   

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
