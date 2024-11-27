from django.db import models
from booking.models import Booking  

class Payment(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Successful', 'Successful'),
        ('Failed', 'Failed'),
    ]

    booking = models.OneToOneField(Booking, related_name="payment", on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=100, unique=True, null=True, blank=True)  # From payment gateway
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for Booking {self.booking.id}: {self.status}"
