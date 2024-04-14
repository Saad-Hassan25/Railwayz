from django.urls import path
from Core.views import*

urlpatterns = [
    path('', homePage, name='home'),
    # Other URL patterns for the core app
]
