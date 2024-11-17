from django.contrib import admin
from .models import ServiceRequest

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('tracking_id', 'customer_name', 'request_type', 'status', 'submission_time', 'resolution_time')
    list_filter = ('status', 'submission_time', 'resolution_time')
    search_fields = ('tracking_id', 'customer_name', 'request_type')
