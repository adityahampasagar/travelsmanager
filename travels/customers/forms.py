from django.forms import ModelForm
from .models import *

class NewCustomer(ModelForm):
	class Meta:
		model = Customer
		fields = ('name', 'mobile_number', 'email', 'address')