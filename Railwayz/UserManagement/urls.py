from django.urls import path
from UserManagement.views import *
app_name = 'UserManagement'

urlpatterns = [
    path('register/', register, name='Register'),
    path('login/', userLogin, name='UserLogin'),
    path('userPage/', userPage, name='UserPage'), 
    path('logout/', userLogout, name='UserLogout'),
    path('contact/', contact, name="contact"),
    path('complaint/', userComplaint, name="complaint"),
    path('services/', services, name="services"),
    path('help/', userHelp, name="help"),
    path('team/', team, name="team"),
    path('terms-and-conditions/', terms, name='terms'),
    path('privacy/', privacy, name='privacy'),
    path('contact-submit/', contact_submit, name='contact_submit')
    # Other URL patterns for the core app
]
