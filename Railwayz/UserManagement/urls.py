from django.urls import path
from UserManagement.views import *
app_name = 'UserManagement'

urlpatterns = [
    path('register/', register, name='Register'),
    path('login/', userLogin, name='UserLogin'),
    path('userPage/', userPage, name='UserPage'), 
    path('logout/', userLogout, name='UserLogout'),



    # Other URL patterns for the core app
]
