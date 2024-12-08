from django.db import models
from restaurant.models import Restaurant

class Menu(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menus')
    availability = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.restaurant.name}"
