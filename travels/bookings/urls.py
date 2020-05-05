from django.urls import path
from . import views

urlpatterns = [
	path('',views.bookings, name='bookings'),
	path('<int:pk>/', views.booking_details, name='booking_details'),
	path('new/', views.new_booking, name='new_booking'),
	path('edit/<int:pk>/', views.edit_booking, name='edit_booking'),
	path('fedit/<int:pk>/', views.edit_booking_extended, name='edit_booking_extended'),
]