from django.contrib import admin
from Bookings.models import * 
# Register your models here.
class BookingInfo(admin.ModelAdmin):
    list_display = ('user','train', 'sourceStation', 'destinationStation', 'journeyDate', 'classType', 'price')
    
    
admin.site.register(Ticket, BookingInfo)