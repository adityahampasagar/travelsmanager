from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *

# Create your views here.
def vehicles(request):
	vehicles = Vehicle.objects.all().order_by('id')
	return render(request, "vehicles.html", {'vehicles': vehicles})

def vehicle_details(request, pk):
	vehicle = get_object_or_404(Vehicle, pk=pk)
	return render(request, "vehicle_details.html", {'vehicle': vehicle})

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