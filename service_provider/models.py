from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    contact_details = models.CharField(max_length=100)
    description = models.TextField()
    check_in_time = models.TimeField()
    check_out_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='hotel_images/')
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.hotel.name}"


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, related_name='rooms', on_delete=models.CASCADE)
    room_type = models.CharField(max_length=255)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    description = models.TextField()
    image = models.ImageField(upload_to='rooms/', blank=True, null=True)  # Field for uploading room images
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.room_type} - {self.hotel.name}"

class Facility(models.Model):
    hotel = models.ForeignKey(Hotel, related_name='facilities', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class BookingRule(models.Model):
    hotel = models.ForeignKey(Hotel, related_name='booking_rules', on_delete=models.CASCADE)
    rule_type = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.rule_type
