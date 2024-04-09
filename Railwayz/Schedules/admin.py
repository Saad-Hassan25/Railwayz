from django.contrib import admin
from Schedules.models import *
# Register your models here.
class ScheduleInfo(admin.ModelAdmin):
    list_display = ('train', 'DepartureStation' ,'ArrivalStation', 'arrival_time', 'departure_time', 'date')
    
    
admin.site.register(TrainSchedule, ScheduleInfo)