from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'booking', 'payment_id', 'amount', 'status', 'created_at']
        read_only_fields = ['payment_id', 'status', 'created_at']
