from django.db import models
from restaurant.models import Restaurant
# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menus')
    availability = models.BooleanField(default=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)