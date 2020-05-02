from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def dashboard(request):
	return render(request, "dashboard.html")