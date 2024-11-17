from django.contrib import admin
from django.urls import path, include
from service_requests import views  # Import views from service_requests

urlpatterns = [
    path('admin/', admin.site.urls),
    path('requests/', include('service_requests.urls')),  # Include app-specific URLs
    path('', views.home, name='home'),  # Home route
]
