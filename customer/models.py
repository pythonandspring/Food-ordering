from django.db import models
from datetime import date, timedelta
from django.db import models



class Student(models.Model):
    CLASS_CHOICES = [
        ('nursery', 'Nursery'),
        ('lkg', 'LKG'),
        ('ukg', 'UKG'),
        ('1st', '1st Class'),
        ('2nd', '2nd Class'),
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    student_class = models.CharField(max_length=10, choices=CLASS_CHOICES)
    phone_number = models.CharField(max_length=15)  # Assuming a simple phone number field
    #class_teacher = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.TextField()
    email = models.EmailField(unique=True)
    date_of_join = models.CharField(max_length=15)
    date_of_leaving = models.CharField(max_length=15)
    second_phone_number = models.CharField(max_length=15, blank=True, null=True)
    photo = models.ImageField(upload_to='static/images/', blank=True, null=True)
    identity_marks = models.TextField(blank=True)
    aadhar_number = models.CharField(max_length=20, blank=True)
    birth_certificate_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

