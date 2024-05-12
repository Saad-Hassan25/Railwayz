from django.shortcuts import render
from django.shortcuts import render
from django.views import View
from django.shortcuts import render
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

