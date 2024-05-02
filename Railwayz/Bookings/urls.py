from django.urls import path
from Bookings.views import *
app_name = 'Bookings'

urlpatterns = [
    path('book-ticket/<int:schedule_id>/', bookTicket, name='BookTicket'),
    path('cancel_ticket/<int:booking_id>/', cancelTicket, name='CancelTicket')

    
]
