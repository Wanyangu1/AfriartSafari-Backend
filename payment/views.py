from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Payment
from .serializers import PaymentSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.select_related('booking').all()
    serializer_class = PaymentSerializer

    @action(detail=True, methods=['post'])
    def process_payment(self, request, pk=None):
        """
        Custom action to process payment for a booking.
        """
        payment = self.get_object()
        booking = payment.booking

        # Simulate payment gateway interaction
        payment_success = True  # Replace with real payment gateway logic
        
        if payment_success:
            payment.status = "Successful"
            payment.payment_id = "txn123"  
            payment.save()
            
            booking.payment_status = "Paid"
            booking.save()

            return Response({
                "message": "Payment processed successfully",
                "payment_id": payment.payment_id,
                "payment_status": payment.status,
            })
        else:
            payment.status = "Failed"
            payment.save()
            return Response({
                "message": "Payment failed",
                "payment_id": None,
                "payment_status": payment.status,
            }, status=status.HTTP_400_BAD_REQUEST)
