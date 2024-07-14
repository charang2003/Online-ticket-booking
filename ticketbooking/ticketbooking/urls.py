# ticketbooking/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('booking.urls')),  # Include booking URLs at the root
    path('accounts/', include('django.contrib.auth.urls')),
]
