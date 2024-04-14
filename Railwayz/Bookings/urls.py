from django.urls import path
from Bookings import views
app_name = 'Bookings'

urlpatterns = [
    path('bookings/', views.train_details, name='bookings'),
    path('train-details/', views.train_details, name='train_details'),
    path('book-ticket/<int:schedule_id>/', views.book_ticket, name='book_ticket'),
    path('cancel_ticket/<int:booking_id>/', views.cancel_ticket, name='cancel_ticket'),


    # Other URL patterns for the core app
]
