from django.contrib import admin
from Schedules.models import *
# Register your models here.
class ScheduleInfo(admin.ModelAdmin):
    list_display = ('Train_Name', 'Source_Station' ,'Destination_Station', 'arrival_time', 'departure_time', 'date')
    
    
    def Train_Name(self, obj):
        return obj.train.name

    def Source_Station(self, obj):
        return obj.ArrivalStation.name

    def Destination_Station(self, obj):
        return obj.DepartureStation.name
    
        
admin.site.register(TrainSchedule, ScheduleInfo)
