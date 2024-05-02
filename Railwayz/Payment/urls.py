from django.urls import path
from Payment.views import *
app_name = 'payment'


urlpatterns = [
    path('billing_page/<int:schedule_id>/<int:passenger_id>/<str:class_type>/<int:num_tickets>/<str:total_amount>/', billing_page, name='billing_page'),
    path('payment_success/', payment_success, name='payment_success')   
]