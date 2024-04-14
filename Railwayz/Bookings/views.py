from django.shortcuts import redirect, render

# Create your views here.
from django.shortcuts import render
from Payment.models import *
from Trains.models import *
from Stations.models import *
from Schedules.models import *
from UserManagement.models import*
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from Bookings.models import *
from django.http import HttpResponse



def train_details(request):
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

    return render(request, 'train_details.html', {
        'available_trains': available_trains,
        'available_stations': available_stations,
        'train_schedules': train_schedules,
    })



def book_ticket(request, schedule_id):
    schedule = TrainSchedule.objects.get(pk=schedule_id)
    passenger_id = request.session.get('passenger_id')
    
    if passenger_id:
        passenger = Passenger.objects.get(pk=passenger_id)
        class_type = request.POST.get('class_type')  # Get the selected class type from the form
        
        if class_type == "economy":
            price = schedule.train.economyClassPrice
        elif class_type == "business":
            price = schedule.train.businessClassPrice
        else:
            # Handle invalid class type, you can redirect to an error page or return an error message
            return HttpResponse("Invalid class type")

        ticket = Ticket(
            user=passenger,
            train=schedule.train,
            sourceStation=schedule.DepartureStation,
            destinationStation=schedule.ArrivalStation,
            journeyDate=schedule.departure_time.date(),
            classType=class_type,  # Save the class type
            price=price,
        )
        ticket.save()
        return redirect('home')  # Redirect to a success page or another appropriate URL
    else:
        # Handle the case where the passenger is not identified (e.g., redirect to a login or selection page)
        return redirect('register')



def cancel_ticket(request, booking_id):
    booking = get_object_or_404(Ticket, pk=booking_id)
    if booking.can_cancel():
        booking.status = 'canceled'
        booking.save()
        messages.success(request, 'Ticket canceled successfully.')
    else:
        messages.error(request, 'Ticket cannot be canceled after 2 hours of booking.')
    return redirect('home')

