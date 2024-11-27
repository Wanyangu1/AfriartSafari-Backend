from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Booking
from payment.models import Payment


@receiver(post_save, sender=Booking)
def create_payment(sender, instance, created, **kwargs):
    """
    Automatically create a Payment instance whenever a Booking is created.
    """
    if created:
        Payment.objects.create(
            booking=instance,
            amount=instance.room.price * instance.number_of_persons  # Example calculation based on room price and persons
        )
