from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.
@login_required()
def customers(request):
	customers = Customer.objects.all().order_by('id')
	return render(request, "customers.html", {'customers': customers})

@login_required()
def customer_details(request, pk):
	customer = get_object_or_404(Customer, pk=pk)
	return render(request, "customer_details.html", {'customer': customer})

@login_required()
def new_customer(request):
	form_title = 'New Customer'
	if request.method == 'POST':
		form = NewCustomer(request.POST)
		if form.is_valid():
			form.save()
			return redirect ('customers')

	else:
		form = NewCustomer()
	
	return render(request, "new_customer.html", {'form': form, 'form_title': form_title})

@login_required()
def edit_customer(request, pk=None):
	customer = get_object_or_404(Customer, pk=pk)
	form_title = 'Edit Customer'
	if request.method == 'POST':
		form = NewCustomer(request.POST, instance=customer)
		if form.is_valid():
			form.save()
			return redirect ('customers')

	else:
		form = NewCustomer(instance=customer)
	
	return render(request, "new_customer.html", {'form': form, 'customer':customer, 'form_title': form_title})