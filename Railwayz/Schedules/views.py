from django.shortcuts import redirect, render, redirect, get_object_or_404
from django.http import HttpResponse
from Payment.models import *
from Trains.models import *
from Stations.models import *
from Schedules.models import *
from UserManagement.models import*
from django.contrib import messages
from Bookings.models import *
from datetime import datetime
from django.db.models import F, ExpressionWrapper, IntegerField
from django.utils import timezone
# Create your views here.



def trainDetails(request):
    current_time = timezone.now()
    available_trains = Train.objects.all()
    available_stations = Station.objects.all()
    train_schedules = TrainSchedule.objects.filter(departure_time__gte=current_time)

    departure_station = request.GET.get('departure')
    arrival_station = request.GET.get('arrival')

    if departure_station and arrival_station:
        train_schedules = train_schedules.filter(
            DepartureStation__name__icontains=departure_station,
            ArrivalStation__name__icontains=arrival_station
        )
        
    for schedule in train_schedules:
        schedule.economy_price = schedule.calculate_price("economy")
        schedule.business_price = schedule.calculate_price("business")

    return render(request, 'schedules.html', 
    {
        'train_schedules': train_schedules,
    })


def departedTrainsDetails(request):
    current_time = timezone.now()
    available_trains = Train.objects.all()
    available_stations = Station.objects.all()
    train_schedules = TrainSchedule.objects.filter(departure_time__lt=current_time)

    departure_station = request.GET.get('departure')
    arrival_station = request.GET.get('arrival')

    if departure_station and arrival_station:
        train_schedules = train_schedules.filter(
            DepartureStation__name__icontains=departure_station,
            ArrivalStation__name__icontains=arrival_station
        )
        
    for schedule in train_schedules:
        if schedule.departure_time < current_time:
            schedule.departure_status = 'Yes' 

        
    for schedule in train_schedules:
        schedule.economy_price = schedule.calculate_price("economy")
        schedule.business_price = schedule.calculate_price("business")

    return render(request, 'departedSchedules.html', 
    {
        'train_schedules': train_schedules,
    })


def vtrainDetails(request):
    current_time = timezone.now()
    available_trains = Train.objects.all()
    available_stations = Station.objects.all()
    train_schedules = TrainSchedule.objects.filter(departure_time__gte=current_time)

    departure_station = request.GET.get('departure')
    arrival_station = request.GET.get('arrival')

    if departure_station and arrival_station:
        train_schedules = train_schedules.filter(
            DepartureStation__name__icontains=departure_station,
            ArrivalStation__name__icontains=arrival_station
        )
        
    for schedule in train_schedules:
        schedule.economy_price = schedule.calculate_price("economy")
        schedule.business_price = schedule.calculate_price("business")

    return render(request, 'vschedules.html', 
    {
        'train_schedules': train_schedules,
    })
