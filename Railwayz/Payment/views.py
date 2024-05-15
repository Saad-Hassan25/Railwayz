import stripe
from Bookings.models import*
from django.shortcuts import redirect, render, redirect, get_object_or_404
from django.http import HttpResponse
from django.conf import settings
from Schedules.models import *
stripe.api_key = settings.STRIPE_SECRET_KEY

def billing_page(request, schedule_id, passenger_id, class_type, num_tickets, total_amount):
    try:
        schedule = TrainSchedule.objects.get(pk=schedule_id)
        passenger = Passenger.objects.get(pk=passenger_id)
                
        if request.method == 'POST':
            try:
                session = create_checkout_session(request, schedule_id=schedule_id, passenger_id=passenger_id, class_type=class_type, num_tickets=num_tickets, total_amount=total_amount)
                return redirect(session.url)

            except Exception as e:
                return HttpResponse(f"Failed to process payment. Error: {e}")
        return render(request, 'billing_page.html', {'schedule': schedule, 'passenger': passenger, 'class_type': class_type, 'num_tickets': num_tickets, 'total_amount': total_amount})


    except Ticket.DoesNotExist:
        return HttpResponse("Booking does not exist!")


def create_checkout_session(request, schedule_id, passenger_id, class_type, num_tickets, total_amount):

    try:
        schedule = TrainSchedule.objects.get(pk=schedule_id)
        passenger = Passenger.objects.get(pk=passenger_id)


        # Create a new Checkout Session
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': f'Train Ticket ({class_type.capitalize()})',
                        },
                        'unit_amount': 100000

                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='http://127.0.0.1:8000/payment_success/',
            cancel_url='http://127.0.0.1:8000/payment_cancel/',
        )


        request.session['schedule_id'] = schedule_id
        request.session['passenger_id'] = passenger_id
        request.session['class_type'] = class_type
        request.session['num_tickets'] = num_tickets
        request.session['total_amount'] = total_amount

        return session


    except Ticket.DoesNotExist:
        return HttpResponse("Booking does not exist!")
    except Exception as e:
        return HttpResponse(f"Failed to create checkout session. Error: {e}")
    
def payment_success(request):
    try:
        # Retrieve necessary information from session data
        schedule_id = request.session.get('schedule_id')
        passenger_id = request.session.get('passenger_id')
        class_type = request.session.get('class_type')
        num_tickets = request.session.get('num_tickets')
        total_amount = request.session.get('total_amount')
 # Convert total_amount to Decimal or float
        total_amount = Decimal(total_amount)  # assuming total_amount is already a string
        
        # Book tickets and decrement available seats
        schedule = TrainSchedule.objects.get(pk=schedule_id)
        passenger = Passenger.objects.get(pk=passenger_id)
        price = total_amount / num_tickets
        
        for _ in range(num_tickets):
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

        # Clear session data
        del request.session['schedule_id']
        del request.session['passenger_id']
        del request.session['class_type']
        del request.session['num_tickets']
        del request.session['total_amount']

        return redirect('UserManagement:UserLogin')

    except Exception as e:
        return HttpResponse(f"Failed to process payment. Error: {e}")
