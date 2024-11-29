from rest_framework import serializers

class PaymentSerializer(serializers.Serializer):
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    booking_id = serializers.IntegerField()

    def validate_total_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("The total amount must be greater than zero.")
        return value

    def validate_booking_id(self, value):
        # Validate that the booking ID exists in your Booking model
        from booking.models import Booking  # Replace with your actual Booking model
        if not Booking.objects.filter(id=value).exists():
            raise serializers.ValidationError("Invalid booking ID.")
        return value
