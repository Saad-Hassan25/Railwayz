from django.db import models
from Trains.models import *
from UserManagement.models import *
from Stations.models import *
from django.utils import timezone
from decimal import Decimal

# Create your models here.
class Ticket(models.Model):
    user = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    sourceStation = models.ForeignKey(Station, related_name='source_tickets', on_delete=models.CASCADE, default = None)
    destinationStation = models.ForeignKey(Station, related_name='destination_tickets', on_delete=models.CASCADE, default= None)
    journeyDate = models.DateField()
    classType = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    booking_time = models.DateTimeField(default=timezone.now)  # Timestamp when the ticket was booked
    status = models.CharField(max_length=20, choices=[('booked', 'Booked'), ('canceled', 'Canceled')], default='booked')

    def __str__(self):
        return f"{self.user} - {self.train.name} - {self.sourceStation.name} to {self.destinationStation.name}"
    
    def canCancel(self):
        time_difference = timezone.now() - self.booking_time
        return time_difference.total_seconds() / 3600 < 2  # Time limit in hours
    
    def calculatePrice(self, classType):
        distance = self.destinationStation.distance - self.sourceStation.distance
        basePrice = self.train.get_base_price(self,classType)
        self.price = Decimal(distance) * basePrice

