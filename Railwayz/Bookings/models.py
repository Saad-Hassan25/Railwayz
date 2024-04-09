from django.db import models
from Trains.models import *
from UserManagement.models import *
from Stations.models import *
from django.conf import settings

# Create your models here.
class Ticket(models.Model):
    user = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    sourceStation = models.ForeignKey(Station, related_name='source_tickets', on_delete=models.CASCADE, default = None)
    destinationStation = models.ForeignKey(Station, related_name='destination_tickets', on_delete=models.CASCADE, default= None)
    journeyDate = models.DateField()
    classType = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)  