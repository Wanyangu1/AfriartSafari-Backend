from django.db import models


class Booking(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
    ]

    room = models.ForeignKey(
        'service_provider.Room',
        related_name="bookings",
        on_delete=models.CASCADE
    )
    full_name = models.CharField(max_length=255)
    number_of_persons = models.PositiveIntegerField()
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    special_requests = models.TextField(blank=True, null=True)
    payment_status = models.CharField(
        max_length=50,
        choices=PAYMENT_STATUS_CHOICES,
        default='Pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.full_name} for {self.room}"
