from django.urls import path
from Core.views import*

urlpatterns = [
    path('', home_page_view, name='home'),
    # Other URL patterns for the core app
]
