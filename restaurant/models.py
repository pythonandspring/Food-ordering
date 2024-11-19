from django.db import models


class Restaurant(models.Model):
    
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, default="Unknown Address")
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    opening_hours = models.CharField(max_length=100, blank=True, null=True)
    cuisine_type = models.CharField(max_length=50, blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    website_url = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    id = models.IntegerField(primary_key=True)
    number_of_products = models.IntegerField()
    product1 = models.CharField(max_length=100, null=True, blank=True)
    product2 = models.CharField(max_length=100, null=True, blank=True)
    product3 = models.CharField(max_length=100, null=True, blank=True)
    price = models.FloatField()
    total = models.FloatField()

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Payment(models.Model):
    customer_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    card_type = models.CharField(max_length=50)
    card_no = models.CharField(max_length=20)