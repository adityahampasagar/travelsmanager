from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.
@login_required()
def vehicles(request):
	vehicles = Vehicle.objects.all().order_by('id')
	return render(request, "vehicles.html", {'vehicles': vehicles})

@login_required()
def vehicle_details(request, pk):
	vehicle = get_object_or_404(Vehicle, pk=pk)
	return render(request, "vehicle_details.html", {'vehicle': vehicle})

@login_required()
def new_vehicle(request):
	form_title = 'New Vehicle'
	if request.method == 'POST':
		form = NewVehicle(request.POST)
		if form.is_valid():
			form.save()
			return redirect ('vehicles')

	else:
		form = NewVehicle()
	
	return render(request, "new_vehicle.html", {'form': form, 'form_title': form_title})

@login_required()
def edit_vehicle(request, pk=None):
	vehicle = get_object_or_404(Vehicle, pk=pk)
	form_title = 'Edit Vehicle'
	if request.method == 'POST':
		form = NewVehicle(request.POST, instance=vehicle)
		if form.is_valid():
			form.save()
			return redirect ('vehicles')

	else:
		form = NewVehicle(instance=vehicle)
	
	return render(request, "new_vehicle.html", {'form': form, 'vehicle':vehicle, 'form_title': form_title})