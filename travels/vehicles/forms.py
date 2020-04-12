from django.forms import ModelForm
from .models import *

class NewVehicle(ModelForm):
	class Meta:
		model = Vehicle
		fields = '__all__'