from django.db import models

# Create your models here.

class Station(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    distance = models.DecimalField(max_digits=10, decimal_places=2, default=1)  # Distance from a reference point

    
    def __str__(self):
        return self.name
