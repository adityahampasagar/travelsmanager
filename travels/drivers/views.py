from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.
@login_required()
def drivers(request):
	drivers = Driver.objects.all().order_by('id')
	return render(request, "drivers.html", {'drivers': drivers})

@login_required()
def driver_details(request, pk):
	driver = get_object_or_404(Driver, pk=pk)
	return render(request, "driver_details.html", {'driver': driver})

@login_required()
def new_driver(request):
	form_title = 'New Driver'
	if request.method == 'POST':
		form = NewDriver(request.POST)
		if form.is_valid():
			form.save()
			return redirect ('drivers')

	else:
		form = NewDriver()
	
	return render(request, "new_driver.html", {'form': form, 'form_title': form_title})

@login_required()
def edit_driver(request, pk=None):
	driver = get_object_or_404(Driver, pk=pk)
	form_title = 'Edit Driver'
	if request.method == 'POST':
		form = NewDriver(request.POST, instance=driver)
		if form.is_valid():
			form.save()
			return redirect ('drivers')

	else:
		form = NewDriver(instance=driver)
	
	return render(request, "new_driver.html", {'form': form, 'driver':driver, 'form_title': form_title})