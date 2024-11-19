from django.db import models
from datetime import date, timedelta
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from customer.models import CustomUser

class deliveryUser(CustomUser):
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
