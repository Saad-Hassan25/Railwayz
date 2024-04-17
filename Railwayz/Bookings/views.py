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

# Create your views here.

def trainDetails(request):
    available_trains = Train.objects.all()
    available_stations = Station.objects.all()
    train_schedules = TrainSchedule.objects.all()

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

    return render(request, 'TrainDetails.html', 
    {
        'train_schedules': train_schedules,
    })

def bookTicket(request, schedule_id):
    schedule = TrainSchedule.objects.get(pk=schedule_id)
    passenger_id = request.session.get('passenger_id')
    
    if passenger_id:
        passenger = Passenger.objects.get(pk=passenger_id)
        class_type = request.POST.get('class_type')  # Get the selected class type from the form
        
        # Check if seats are available
        if class_type == "economy":
            available_seats = schedule.available_economy_seats
        elif class_type == "business":
            available_seats = schedule.available_business_seats
        else:
            return HttpResponse("Invalid class type")

        if available_seats <= 0:
            return HttpResponse("No seats available for booking")

        # Check for price
        if class_type == "economy":
            price = schedule.train.economyClassPrice
        elif class_type == "business":
            price = schedule.train.businessClassPrice
        else:
            return HttpResponse("Invalid class type")

        ticket = Ticket(
            user=passenger,
            train=schedule.train,
            sourceStation=schedule.DepartureStation,
            destinationStation=schedule.ArrivalStation,
            journeyDate=schedule.departure_time.date(),
            classType=class_type, 
            price=price,
        )
        ticket.save()
        schedule.decrement_available_seats(class_type)
        return redirect('UserManagement:UserPage')
    else:
        return redirect('UserManagement:UserLogin')


def cancelTicket(request, booking_id):
    booking = get_object_or_404(Ticket, pk=booking_id)
    if booking.canCancel():
        booking.status = 'canceled'
        booking.save()
        schedule = TrainSchedule.objects.get(train=booking.train, DepartureStation=booking.sourceStation, ArrivalStation=booking.destinationStation)
        schedule.increment_available_seats(booking.classType)

        messages.success(request, 'Ticket canceled successfully.')
    else:
        messages.error(request, 'Ticket cannot be canceled after 2 hours of booking.')
    return redirect('home')

