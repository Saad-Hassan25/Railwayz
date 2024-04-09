from django.urls import path
from UserManagement import views
app_name = 'UserManagement'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),

    # Other URL patterns for the core app
]
