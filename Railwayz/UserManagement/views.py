from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Passenger
from .forms import PassengerRegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
# Example: Storing Passenger ID in a Session Variable
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth import logout
from Bookings.models import *

def register(request):
    if request.method == 'POST':
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        cnic = request.POST.get('cnic')
        phoneNumber = request.POST.get('phoneNumber')
        gender = request.POST.get('gender')
        
        user = User.objects.create_user(username=email, email=email, password=password)
        
        passenger = Passenger.objects.create(
            firstName=firstName,
            lastName=lastName,
            email=email,
            password=password,
            address=address,
            cnic=cnic,
            phoneNumber=phoneNumber,
            gender=gender,
            user=user
        )
        user.save()
        passenger.save()
        
        return redirect('home')  # Redirect to home page after successful registration
    else:
        return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        if user is not None:
            try:
                passenger = Passenger.objects.get(user=user)
                request.session['passenger_id'] = passenger.id
                login(request, user)
                return redirect('UserManagement:user_page')
            except Passenger.DoesNotExist:
                error_message = 'Passenger does not exist'
        else:
            error_message = 'Invalid email or password'
        return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')


def user_page(request):
    passenger_id = request.session.get('passenger_id')
    if passenger_id:
        try:
            bookings = Ticket.objects.filter(user_id=passenger_id)
            return render(request, 'userPage.html', {'bookings': bookings})
        except Ticket.DoesNotExist:
            return render(request, 'userPage.html', {'bookings': None})
    else:
        return redirect('UserManagement:user_login')



def user_logout(request):
    logout(request)
    return redirect('home')  
