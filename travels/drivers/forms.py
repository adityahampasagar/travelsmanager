from django.forms import ModelForm
from .models import *

class NewDriver(ModelForm):
	class Meta:
		model = Driver
		fields = '__all__'