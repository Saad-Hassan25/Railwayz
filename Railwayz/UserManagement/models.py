from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

firstName = models.CharField(max_length = 30)
lastName = models.CharField(max_length = 30)
email = models.CharField(max_length = 30)
cnic = models.CharField(max_length = 13)
address = models.models.TextField()
phoneNumber = models.CharField(max_length = 11)
gender = models.CharField(max_length = 6)

