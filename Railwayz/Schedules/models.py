from django.db import models
from Trains.models import *
from Stations.models import *
from datetime import date



# Create your models here.

class TrainSchedule(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    arrival_time = models.DateTimeField()
    departure_time = models.DateTimeField()
    date = models.DateField(default=date.today)

