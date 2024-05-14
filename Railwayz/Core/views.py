from django.shortcuts import render
from django.shortcuts import render
from django.views import View
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
# Create your views here.

def homePage(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def help(request):
    return render(request,"help.html")

def privacy(request):
    return render(request,"privacy.html")

def services(request):
    return render(request,"services.html")


def team(request):
    return render(request,"team.html")

def terms(request):
    return render(request, 'terms.html')

def contact_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        # Send email
        send_mail(
            'Contact Form Submission',
            f'Name: {name}\nEmail: {email}\nMessage: {message}',
            email,  # Replace with your email address
            ['l215252@lhr.nu.edu.pk'],  # Replace with recipient email address
            fail_silently=False,
        )

        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})

