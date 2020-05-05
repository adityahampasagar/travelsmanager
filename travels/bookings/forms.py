from django import forms
from django.forms import ModelForm
from .models import *

class NewBooking(ModelForm):
	class Meta:
		model = Booking
		fields = '__all__'

class Booking_Extended_Form(ModelForm):
	class Meta:
		model = Booking_Extended
		fields = '__all__'
		widgets = {'booking': forms.HiddenInput()}