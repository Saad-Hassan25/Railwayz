from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Passenger
from .forms import PassengerRegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth import logout
from Bookings.models import *
from django.http import JsonResponse
from django.core.mail import send_mail, EmailMessage
from Railwayz import settings
from . models import *
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from . tokens import generate_token 
from django.contrib.auth import update_session_auth_hash

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
        user.first_name = firstName
        user.last_name = lastName
        user.email = email
        user.is_active = False       
        user.save()
        passenger.save()
        sendConfirmationEmail(request, user)

        return redirect('UserManagement:RegistrationComplete')
    else:
        return render(request, 'register.html')

def userLogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        if user is not None:
            try:
                passenger = Passenger.objects.get(user=user)
                request.session['passenger_id'] = passenger.id
                login(request, user)
                return redirect('UserManagement:UserPage')
            except Passenger.DoesNotExist:
                error_message = 'Passenger does not exist'
        else:
            messages.error(request,"invalid credentials")
            return redirect('UserManagement:incorrectDetails') 

    else:
        return render(request, 'login.html')


def userPage(request):
    passenger_id = request.session.get('passenger_id')
    if passenger_id:
        try:
            bookings = Ticket.objects.filter(user_id=passenger_id)
            return render(request, 'userPage.html', {'bookings': bookings})
        except Ticket.DoesNotExist:
            return render(request, 'userPage.html', {'bookings': None})
    else:
        return redirect('UserManagement:UserLogin')



def userLogout(request):
    logout(request)
    return redirect('home')  


def registrationComplete(request):
    return render(request,"successful.html")



def sendConfirmationEmail(request, myUser):
    current_site = get_current_site(request)
    emailSubject = "Railwayz - Confirm your Email"
    message2 = render_to_string('confirmationEmail.html',{
            
            'name': myUser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myUser.pk)),
            'token': generate_token.make_token(myUser)
        })
    email = EmailMessage(
        emailSubject,
        message2,
        settings.EMAIL_HOST_USER,
        [myUser.email],
    )
    email.fail_silently = True
    email.send()
    
def activate(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request,myuser)
        return redirect('UserManagement:UserLogin')
    else:
        return render(request,'registrationFailed.html')

def activationFailed(request):
    return render(request,"registrationFailed.html")


def incorrectDetails(request):
    return render(request,"incorrectDetails.html")

def forgetPassword(request):
    return render(request,"passwordReset.html")

