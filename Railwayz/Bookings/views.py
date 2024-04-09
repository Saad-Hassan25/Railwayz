from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from Payment.models import *
from Trains.models import *
from Stations.models import *
from Schedules.models import *

def train_details(request):
    available_trains = Train.objects.all()
    available_stations = Station.objects.all()
    train_schedules = TrainSchedule.objects.all()

    return render(request, 'train_details.html', {
        'available_trains': available_trains,
        'available_stations': available_stations,
        'train_schedules': train_schedules,
    })
