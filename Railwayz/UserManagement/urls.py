from django.urls import path
from UserManagement import views
app_name = 'UserManagement'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('userPage/', views.user_page, name='user_page'),  # URL pattern for the user page
    path('logout/', views.user_logout, name='user_logout'),



    # Other URL patterns for the core app
]
