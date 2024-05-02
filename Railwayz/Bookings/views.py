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
import stripe
from django.conf import settings


# Create your views here.

def bookTicket(request, schedule_id):
    schedule = TrainSchedule.objects.get(pk=schedule_id)
    passenger_id = request.session.get('passenger_id')
    
    if passenger_id:
        passenger = Passenger.objects.get(pk=passenger_id)
        class_type = request.POST.get('class_type')  # Get the selected class type from the form
        num_tickets = int(request.POST.get('num_tickets', 1))  # Get the number of tickets to book
                
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
        
        total_amount = price * num_tickets
        return redirect('Payment:billing_page', schedule_id=schedule_id, passenger_id=passenger_id, class_type=class_type, num_tickets=num_tickets, total_amount=total_amount)

        
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


