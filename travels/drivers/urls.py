from django.urls import path
from . import views

urlpatterns = [
	path('',views.drivers, name='drivers'),
	path('<int:pk>/', views.driver_details, name='driver_details'),
	path('new/', views.new_driver, name='new_driver'),
	path('edit/<int:pk>/', views.edit_driver, name='edit_driver'),
]