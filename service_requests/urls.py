from django.urls import path
from . import views  # Import views from the app

urlpatterns = [
    path('submit/', views.submit_request, name='submit_request'),  # Submit request page
    path('track/', views.track_request, name='track_request'),    # Tracking page
]
