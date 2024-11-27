from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Booking
from .serializers import BookingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.select_related('room__hotel').all()
    serializer_class = BookingSerializer

    @action(detail=True, methods=['post'])
    def process_payment(self, request, pk=None):
        """
        Custom action to handle payment processing.
        """
        booking = self.get_object()
        
        # Simulate payment processing (you can replace this with actual payment gateway logic)
        payment_success = True  # Replace with actual payment gateway response logic
        
        if payment_success:
            booking.payment_status = "Paid"
            booking.save()
            return Response({
                "message": "Payment processed successfully", 
                "payment_id": "pid123",  # Payment ID (use real ID from payment gateway)
                "booking_id": booking.id
            })
        else:
            return Response({
                "message": "Payment failed",
                "payment_id": None,
                "booking_id": booking.id
            }, status=400)
