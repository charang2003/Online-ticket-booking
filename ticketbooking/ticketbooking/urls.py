"""
URL configuration for ticketbooking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'booking'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.event_list, name='event_list'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('ticket/<int:ticket_id>/book/', views.book_ticket, name='book_ticket'),
    path('bookings/', views.booking_list, name='booking_list'),
    path('booking/', include('booking.urls')),
    path('accounts/', include('django.contrib.auth.urls')), 
]
