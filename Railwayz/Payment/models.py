from django.db import models
from Bookings.models import *
# Create your models here.
class Payment(models.Model):
    booking = models.OneToOneField(Ticket, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50)  # e.g., Credit Card, Debit Card
    transaction_id = models.CharField(max_length=50, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[("SUCCESS", "Successful"), ("FAILED", "Failed")])
