from django.urls import path
from . import views

urlpatterns = [
	path('',views.vehicles, name='vehicles'),
	path('<int:pk>/', views.vehicle_details, name='vehicle_details'),
	path('new/', views.new_vehicle, name='new_vehicle'),
	path('edit/<int:pk>/', views.edit_vehicle, name='edit_vehicle'),
]