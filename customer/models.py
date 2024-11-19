from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name