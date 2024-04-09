from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Passenger
from .forms import PassengerRegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login

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
            auth_login(request, user)
            return redirect('booking')  # Redirect to home page after successful login
        else:
            error_message = 'Invalid email or password'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')
