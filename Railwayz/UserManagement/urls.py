from django.urls import path
from UserManagement.views import *
app_name = 'UserManagement'

urlpatterns = [
    path('register/', register, name='Register'),
    path('login/', userLogin, name='UserLogin'),
    path('userPage/', userPage, name='UserPage'), 
    path('logout/', userLogout, name='UserLogout'),
    path('contact/', userContact, name="contact"),
    path('complaint/', userComplaint, name="complaint"),
    path('services/', services, name="services"),
    path('help/', userHelp, name="help"),
    path('team/', team, name="team"),
    # Other URL patterns for the core app
]
