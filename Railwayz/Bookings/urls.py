from django.urls import path
from Bookings import views
app_name = 'Bookings'

urlpatterns = [
    path('bookings/', views.train_details, name='bookings'),
    # Other URL patterns for the core app
]
