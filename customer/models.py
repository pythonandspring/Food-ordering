from django.db import models
from datetime import date, timedelta
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User
from ordering.models import FoodItem

class Customer(models.Model):
    first_name = models.CharField(max_length=50, default='FirstName')
    last_name = models.CharField(max_length=50, default='LastName')
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    food_items = models.ManyToManyField(FoodItem)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    status = models.CharField(max_length=1, choices=[
        ('P', 'Pending'),
        ('C', 'Completed'),
        ('A', 'Canceled'),
    ], default='P')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} by {self.customer.first_name} {self.customer.last_name}"

class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50,default='Unknown')
    status = models.CharField(max_length=10, choices=[
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid')
    ],default='unpaid')
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.id} for order {self.order.id}"

# class Student(models.Model):

#     CLASS_CHOICES = [
#         ('nursery', 'Nursery'),
#         ('lkg', 'LKG'),
#         ('ukg', 'UKG'),
#         ('1st', '1st Class'),
#         ('2nd', '2nd Class'),
#     ]

#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     father_name = models.CharField(max_length=255)
#     mother_name = models.CharField(max_length=255)
#     student_class = models.CharField(max_length=10, choices=CLASS_CHOICES)
#     phone_number = models.CharField(max_length=15)  # Assuming a simple phone number field
#     class_teacher = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
#     address = models.TextField()
#     email = models.EmailField(unique=True)
#     date_of_join = models.CharField(max_length=15)
#     date_of_leaving = models.CharField(max_length=15)
#     second_phone_number = models.CharField(max_length=15, blank=True, null=True)
#     photo = models.ImageField(upload_to='static/images/', blank=True, null=True)
#     identity_marks = models.TextField(blank=True)
#     aadhar_number = models.CharField(max_length=20, blank=True)
#     birth_certificate_number = models.CharField(max_length=20, blank=True)

#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'

# class Customer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     address = models.TextField()
#     phone_number = models.CharField(max_length=15)

#     def __str__(self):
#         return self.user.username

# class Order(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     status = models.CharField(max_length=20)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"Order {self.id} by {self.customer.user.username}"

# class Payment(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     payment_date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Payment {self.id} for order {self.order.id}"

