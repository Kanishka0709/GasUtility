from django.shortcuts import render
from django.http import HttpResponse
import random
import string
from .models import ServiceRequest
def generate_tracking_id():
    """Generate a unique 12-character tracking ID."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))

# Home view
def home(request):
    return HttpResponse("<h1>Welcome to Gas Utility Service</h1>")


# Submit Request view
def submit_request(request):
    if request.method == 'POST':
        # Get form data
        customer_name = request.POST.get('customer_name')
        request_type = request.POST.get('request_type')
        description = request.POST.get('description')

        # Create a new service request
        tracking_id = generate_tracking_id()
        service_request = ServiceRequest.objects.create(
            tracking_id=tracking_id,
            customer_name=customer_name,
            request_type=request_type,
            description=description
        )

        # Pass the tracking ID to the success page
        return render(request, 'service_requests/submit_success.html', {'tracking_id': tracking_id})

    # Render the submission form
    return render(request, 'service_requests/submit_request.html')

# Track Request view
def track_request(request):
    if request.method == 'POST':
        tracking_id = request.POST.get('tracking_id')

        # Fetch the service request from the database
        try:
            service_request = ServiceRequest.objects.get(tracking_id=tracking_id)
            return render(request, 'service_requests/track_result.html', {'service_request': service_request})
        except ServiceRequest.DoesNotExist:
            error_message = "Tracking ID not found. Please check and try again."
            return render(request, 'service_requests/track_requests.html', {'error_message': error_message})

    # Render the tracking form
    return render(request, 'service_requests/track_requests.html')
from django.shortcuts import render
from django.http import HttpResponse

# Home View
def home(request):
    # Render the home template
    return render(request, 'service_requests/home.html')

