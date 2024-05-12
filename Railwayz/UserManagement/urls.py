from django.urls import path
from UserManagement.views import *
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'UserManagement'

urlpatterns = [
    
    path('register/', register, name='Register'),
    path('login/', userLogin, name='UserLogin'),
    path('userPage/', userPage, name='UserPage'), 
    path('logout/', userLogout, name='UserLogout'),
    path('registrationComplete', registrationComplete, name="RegistrationComplete"),
    path('activate/<uidb64>/<token>', activate, name='activate'),  
    path('activationFailed', activationFailed, name="activationFailed"),
    path('incorrectDetails', incorrectDetails, name='incorrectDetails'),
    path('forgetPassword', forgetPassword, name="forgetPassword"),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='passwordReset.html'), name='password_reset'),
    path('password_reset/done/', password_reset_done, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    # Other URL patterns for the core app
]
