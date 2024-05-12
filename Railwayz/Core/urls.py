from django.urls import path
from Core.views import*

app_name = 'Core'

urlpatterns = [
    path('', homePage, name='home'),
    path('contact/', contact, name='contact'),
    path('help/', help, name="help"),
    path('privacy/', privacy, name='privacy'),
    path('services/', services, name="services"),
    path('team/', team, name="team"),
    path('terms-and-conditions/', terms, name='terms')   
    
    # Other URL patterns for the core app
]
