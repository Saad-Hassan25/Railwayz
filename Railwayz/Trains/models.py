from django.db import models

# Create your models here.
class Train(models.Model):
    name = models.CharField(max_length=100)
    economy_capacity = models.IntegerField(default=0)  # Capacity for economy class
    business_capacity = models.IntegerField(default=0)  # Capacity for business class
    economyClassPrice = models.DecimalField(max_digits=10, decimal_places=2)
    businessClassPrice = models.DecimalField(max_digits=10, decimal_places=2)
    
    @property
    def total_capacity(self):
        return self.economy_capacity + self.business_capacity
    
    def __str__(self):
        return self.name

    
    def getBasePrice(self, class_type):
        if class_type == 'Economy':
            return self.economyClassPrice
        elif class_type == 'Business':
            return self.businessClassPrice
        else:
            return 0  # Default to 0 for unknown class types





    
