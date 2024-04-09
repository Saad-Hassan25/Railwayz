from django.db import models
from django.contrib.auth.models import User

class Passenger(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)  
    password = models.TextField()
    address = models.TextField()
    cnic = models.CharField(max_length=15)
    phoneNumber = models.CharField(max_length=15)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='passenger', null=True)
