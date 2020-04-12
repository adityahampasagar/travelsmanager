from django.forms import ModelForm
from .models import *

class NewBooking(ModelForm):
	class Meta:
		model = Booking
		fields = '__all__'