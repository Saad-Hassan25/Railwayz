from django.urls import path
from Schedules.views import *
app_name = 'Schedules'

urlpatterns = [
    path('bookings/', trainDetails, name='bookings'),
    path('train-details/', trainDetails, name='TrainDetails'),
    path('departed-trains/', departedTrainsDetails, name='DepartedTrains'),
    path('vtrain-details/', vtrainDetails, name='vTrainDetails')
]
