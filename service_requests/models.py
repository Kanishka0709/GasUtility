from django.db import models
from django.utils.timezone import now

class ServiceRequest(models.Model):
    customer_name = models.CharField(max_length=100)
    request_type = models.CharField(max_length=100)
    details = models.TextField()
    file_attachment = models.FileField(upload_to='attachments/', null=True, blank=True)
    status = models.CharField(max_length=20, default="Pending")
    submission_date = models.DateTimeField(auto_now_add=True)
    resolution_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.customer_name} - {self.request_type} - {self.status}"
class Account(models.Model):
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.customer_name
    

class ServiceRequest(models.Model):
    tracking_id = models.CharField(max_length=12, unique=True)  # Unique tracking ID
    customer_name = models.CharField(max_length=100)
    request_type = models.CharField(max_length=100)
    description = models.TextField()
    submission_time = models.DateTimeField(default=now)  # Auto-set submission time
    resolution_time = models.DateTimeField(null=True, blank=True)  # Can be updated later
    status = models.CharField(max_length=50, default='Pending')  # Status of request

    def __str__(self):
        return f"{self.tracking_id} - {self.customer_name}"