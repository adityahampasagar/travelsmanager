from django.urls import path
from . import views

urlpatterns = [
	path('',views.customers, name='customers'),
	path('<int:pk>/', views.customer_details, name='customer_details'),
	path('new/', views.new_customer, name='new_customer'),
	path('edit/<int:pk>/', views.edit_customer, name='edit_customer'),
]