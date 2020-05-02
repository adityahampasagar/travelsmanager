from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('dashboard.urls')),
    path('bookings/',include('bookings.urls')),
    path('customers/',include('customers.urls')),
    path('drivers/',include('drivers.urls')),
    path('vehicles/',include('vehicles.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
