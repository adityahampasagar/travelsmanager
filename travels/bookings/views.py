from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.
@login_required()
def bookings(request):
	bookings = Booking.objects.all().order_by('id')
	return render(request, "bookings.html", {'bookings': bookings})

@login_required()
def booking_details(request, pk):
	booking = get_object_or_404(Booking, pk=pk)
	booking_extended = Booking_Extended.objects.filter(pk=pk).first()
	return render(request, "booking_details.html", {'booking': booking, 'booking_extended': booking_extended})

@login_required()
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

@login_required()
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

@login_required()
def edit_booking_extended(request, pk=None):
	if Booking_Extended.objects.filter(pk=pk).exists():

		booking = Booking_Extended.objects.filter(pk=pk).first()
		form_title = 'Edit Financials for Booking with ID ' + ": " + str(pk)
		if request.method == 'POST':
			form = Booking_Extended_Form(request.POST, instance=booking)
			if form.is_valid():
				form.save()
				return redirect ('bookings')

		else:
			form = Booking_Extended_Form(instance=booking)
	
		return render(request, "booking_extended.html", {'form': form, 'booking':booking, 'form_title': form_title, 'pk': pk})

	else:
		form_title = 'New Financials for Booking with ID ' + ": " + str(pk)
		if request.method == 'POST':
			form = Booking_Extended_Form(request.POST)
			if form.is_valid():
				form.save()
				return redirect ('bookings')

		else:
			form = Booking_Extended_Form()
	
		return render(request, "booking_extended.html", {'form': form, 'form_title': form_title, 'pk': pk})
