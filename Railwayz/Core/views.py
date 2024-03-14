from django.shortcuts import render
from django.shortcuts import render
from django.views import View
from django.shortcuts import render
# Create your views here.

def home_page_view(request):
    return render(request, 'home.html')
