from django.db import models
from Trains.models import *
from Stations.models import *
from datetime import date



# Create your models here.

class TrainSchedule(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    DepartureStation = models.ForeignKey(Station, related_name='departure_schedules', on_delete=models.CASCADE, default=None)
    ArrivalStation = models.ForeignKey(Station, related_name='arrival_schedule', on_delete=models.CASCADE, default=None)
    arrival_time = models.DateTimeField()
    departure_time = models.DateTimeField()
    date = models.DateField(default=date.today)
    
   


