from rest_framework import serializers
from .models import Booking
from service_provider.serializers import RoomSerializer  # Import RoomSerializer from the service_provider app

class BookingSerializer(serializers.ModelSerializer):
    room_details = RoomSerializer(source="room", read_only=True)  # Include room details in response

    class Meta:
        model = Booking
        fields = [
            'id',
            'room',
            'room_details',
            'full_name',
            'number_of_persons',
            'check_in_date',
            'check_out_date',
            'special_requests',
            'payment_status',
            'created_at',
        ]
