from django.contrib import admin
from Trains.models import *
# Register your models here.
class TrainInfo(admin.ModelAdmin):
    list_display = ('name', 'type', 'capacity', 'economyClassPrice', 'businessClassPrice')
    
    
admin.site.register(Train, TrainInfo)