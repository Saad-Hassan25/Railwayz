from django.contrib import admin
from Stations.models import *
# Register your models here.
class StationInfo(admin.ModelAdmin):
    list_display = ('name', 'location')
    

admin.site.register(Station, StationInfo)