from django.db import models

# Create your models here.
class Train(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    capacity = models.IntegerField()
    economyClassPrice = models.DecimalField(max_digits=10, decimal_places=2)
    businessClassPrice = models.DecimalField(max_digits=10, decimal_places=2)


    
