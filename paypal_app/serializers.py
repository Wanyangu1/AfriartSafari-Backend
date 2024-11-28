from rest_framework import serializers

class PaymentSerializer(serializers.Serializer):
    
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2)

    def validate_total_amount(self, value):
        # Ensure that the amount is positive and greater than zero
        if value <= 0:
            raise serializers.ValidationError("The total amount must be greater than zero.")
        return value
