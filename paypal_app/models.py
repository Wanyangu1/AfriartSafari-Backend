from django.db import models

class Payment(models.Model):
    payment_id = models.CharField(max_length=255, unique=True)
    booking_id = models.CharField(max_length=255)  # You can also use IntegerField if booking ID is numeric
    payer_id = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    status = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.payment_id} - {self.status}"
