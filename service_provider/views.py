from rest_framework import viewsets
from .models import Hotel, Room, Facility, BookingRule, HotelImage
from .serializers import HotelSerializer, RoomSerializer, FacilitySerializer, BookingRuleSerializer, HotelImageSerializer

class HotelViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing hotels. Includes related rooms, facilities, booking rules, and images.
    """
    queryset = Hotel.objects.prefetch_related('rooms', 'facilities', 'booking_rules', 'images').all()
    serializer_class = HotelSerializer

class RoomViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing hotel rooms.
    """
    queryset = Room.objects.select_related('hotel').all()  # Optimize with `select_related` for hotel
    serializer_class = RoomSerializer

class FacilityViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing hotel facilities.
    """
    queryset = Facility.objects.select_related('hotel').all()  # Optimize with `select_related` for hotel
    serializer_class = FacilitySerializer

class BookingRuleViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing hotel booking rules.
    """
    queryset = BookingRule.objects.select_related('hotel').all()  # Optimize with `select_related` for hotel
    serializer_class = BookingRuleSerializer

class HotelImageViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing hotel images.
    """
    queryset = HotelImage.objects.all()
    serializer_class = HotelImageSerializer
