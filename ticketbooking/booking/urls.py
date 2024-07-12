# booking/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.event_list, name='event_list'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('ticket/<int:ticket_id>/book/', views.book_ticket, name='book_ticket'),
    path('bookings/', views.booking_list, name='booking_list'),
]
