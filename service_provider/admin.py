from django.contrib import admin
from .models import Hotel, Room, Facility, BookingRule, HotelImage

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'contact_details', 'created_at', 'updated_at', 'image_thumbnail')
    search_fields = ('name', 'location')
    list_filter = ('location',)
    ordering = ('-created_at',)

    def image_thumbnail(self, obj):
        # Check if the hotel has related images
        if obj.images.exists():
            image = obj.images.first()  # Get the first image from related images
            return f'<img src="{image.image.url}" width="50" height="50" />'  # Display the first image
        return 'No Image'
    
    image_thumbnail.allow_tags = True
    image_thumbnail.short_description = 'Image Preview'

@admin.register(HotelImage)
class HotelImageAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'image', 'description')
    search_fields = ('hotel__name',)  # You can search by hotel name


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_type', 'hotel', 'price_per_night', 'availability', 'created_at', 'updated_at', 'image_thumbnail')
    list_filter = ('availability', 'hotel')
    search_fields = ('room_type',)
    ordering = ('-created_at',)

    def image_thumbnail(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="50" height="50" />'
        return 'No Image'
    image_thumbnail.allow_tags = True
    image_thumbnail.short_description = 'Image Preview'

@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ('name', 'hotel', 'description')
    search_fields = ('name',)
    list_filter = ('hotel',)
    ordering = ('name',)

@admin.register(BookingRule)
class BookingRuleAdmin(admin.ModelAdmin):
    list_display = ('rule_type', 'hotel', 'description')
    search_fields = ('rule_type',)
    list_filter = ('hotel',)
    ordering = ('rule_type',)
