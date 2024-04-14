from django.db import models

# Create your models here.
class Train(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    economyClassPrice = models.DecimalField(max_digits=10, decimal_places=2)
    businessClassPrice = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name
    
    def getBasePrice(self, class_type):
        if class_type == 'Economy':
            return self.economyClassPrice
        elif class_type == 'Business':
            return self.businessClassPrice
        else:
            return 0  # Default to 0 for unknown class types





    
