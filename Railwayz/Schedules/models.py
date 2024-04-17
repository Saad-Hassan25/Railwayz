from django.db import models
from Trains.models import *
from Stations.models import *
from datetime import date
from django.db.models import F
from Bookings.models import *
# Create your models here.


class TrainSchedule(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    DepartureStation = models.ForeignKey(Station, related_name='departure_schedules', on_delete=models.CASCADE, default=None)
    ArrivalStation = models.ForeignKey(Station, related_name='arrival_schedule', on_delete=models.CASCADE, default=None)
    arrival_time = models.DateTimeField()
    departure_time = models.DateTimeField()
    date = models.DateField(default=date.today)
    
    @property
    def available_economy_seats(self):
        booked_tickets = Ticket.objects.filter(train=self.train, sourceStation=self.DepartureStation, destinationStation=self.ArrivalStation, classType='Economy').count()
        return self.train.economy_capacity - booked_tickets

    @property
    def available_business_seats(self):
        booked_tickets = Ticket.objects.filter(train=self.train, sourceStation=self.DepartureStation, destinationStation=self.ArrivalStation, classType='Business').count()
        return self.train.business_capacity - booked_tickets
    
    def decrement_available_seats(self, class_type):
        if class_type == "economy":
            self.train.economy_capacity -= 1
        elif class_type == "business":
            self.train.business_capacity -= 1
        self.train.save()
        
    def increment_available_seats(self, class_type):
        if class_type == "economy":
            self.train.economy_capacity += 1
        elif class_type == "business":
            self.train.business_capacity += 1
        self.train.save()
        
    def calculate_price(self, class_type):
        if class_type == "economy":
            base_price = self.train.economyClassPrice
        elif class_type == "business":
            base_price = self.train.businessClassPrice
        else:
            raise ValueError("Invalid class type")

        
        return base_price


