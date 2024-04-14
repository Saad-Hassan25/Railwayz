from django.contrib import admin
from Bookings.models import * 
# Register your models here.
class BookingInfo(admin.ModelAdmin):
    list_display = ('id', 'Train_Name', 'Source_Station', 'Destination_Station', 'journeyDate', 'classType', 'price')
    
    def Train_Name(self, obj):
        return obj.train.name

    def Source_Station(self, obj):
        return obj.sourceStation.name

    def Destination_Station(self, obj):
        return obj.destinationStation.name
    
admin.site.register(Ticket, BookingInfo)

