from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *

# Create your views here.
def bookings(request):
	bookings = Booking.objects.all().order_by('id')
	return render(request, "bookings.html", {'bookings': bookings})

def booking_details(request, pk):
	booking = get_object_or_404(Booking, pk=pk)
	return render(request, "booking_details.html", {'booking': booking})

def new_booking(request):
	form_title = 'New Booking'
	if request.method == 'POST':
		form = NewBooking(request.POST)
		if form.is_valid():
			form.save()
			return redirect ('bookings')

	else:
		form = NewBooking()
	
	return render(request, "new_booking.html", {'form': form, 'form_title': form_title})

def edit_booking(request, pk=None):
	booking = get_object_or_404(Booking, pk=pk)
	form_title = 'Edit Booking'
	if request.method == 'POST':
		form = NewBooking(request.POST, instance=booking)
		if form.is_valid():
			form.save()
			return redirect ('bookings')

	else:
		form = NewBooking(instance=booking)
	
	return render(request, "new_booking.html", {'form': form, 'booking':booking, 'form_title': form_title})