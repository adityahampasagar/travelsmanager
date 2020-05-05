from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Booking)
admin.site.register(Booking_Extended)