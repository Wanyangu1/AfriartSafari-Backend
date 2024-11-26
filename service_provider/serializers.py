from rest_framework import serializers
from .models import Hotel, Room, Facility, BookingRule, HotelImage

class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = ['id', 'hotel','image', 'description']

class HotelSerializer(serializers.ModelSerializer):
    rooms = serializers.PrimaryKeyRelatedField(many=True, read_only=True)  # List of related room IDs
    facilities = serializers.PrimaryKeyRelatedField(many=True, read_only=True)  # List of related facility IDs
    booking_rules = serializers.PrimaryKeyRelatedField(many=True, read_only=True)  # List of related booking rule IDs

    class Meta:
        model = Hotel
        fields = [
            'id',
            'name',
            'location',
            'contact_details',
            'description',
            'check_in_time',
            'check_out_time',
            'rooms',
            'facilities',
            'booking_rules',
            'created_at',
            'updated_at',
        ]

class RoomSerializer(serializers.ModelSerializer):
    hotel = serializers.StringRelatedField()  # Display hotel name instead of ID
    hotel_id = serializers.PrimaryKeyRelatedField(queryset=Hotel.objects.all())  # For assigning hotel by ID

    class Meta:
        model = Room
        fields = [
            'id',
            'hotel',
            'hotel_id',
            'room_type',
            'price_per_night',
            'availability',
            'description',
            'image',
            'created_at',
            'updated_at',
        ]

class FacilitySerializer(serializers.ModelSerializer):
    hotel = serializers.StringRelatedField()  # Display hotel name instead of ID
    hotel_id = serializers.PrimaryKeyRelatedField(queryset=Hotel.objects.all())  # For assigning hotel by ID

    class Meta:
        model = Facility
        fields = [
            'id',
            'hotel',
            'hotel_id',
            'name',
            'description',
        ]

class BookingRuleSerializer(serializers.ModelSerializer):
    hotel = serializers.StringRelatedField()  # Display hotel name instead of ID
    hotel_id = serializers.PrimaryKeyRelatedField(queryset=Hotel.objects.all())  # For assigning hotel by ID

    class Meta:
        model = BookingRule
        fields = [
            'id',
            'hotel',
            'hotel_id',
            'rule_type',
            'description',
        ]
