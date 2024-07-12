from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Event, Ticket, Booking
from .forms import BookingForm

def event_list(request):
    events = Event.objects.all()
    return render(request, 'booking/event_list.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    tickets = Ticket.objects.filter(event=event)
    return render(request, 'booking/event_detail.html', {'event': event, 'tickets': tickets})

@login_required
def book_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.ticket = ticket
            booking.save()
            return redirect('booking:booking_list')
    else:
        form = BookingForm()
    return render(request, 'booking/book_ticket.html', {'form': form, 'ticket': ticket})

def home(request):
    return render(request, 'booking/home.html')

@login_required
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/booking_list.html', {'bookings': bookings})
