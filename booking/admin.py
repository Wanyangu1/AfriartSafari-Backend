from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'room',
        'number_of_persons',
        'check_in_date',
        'check_out_date',
        'payment_status',
        'created_at',
    )
    list_filter = ('payment_status', 'check_in_date', 'check_out_date', 'created_at')
    search_fields = ('full_name', 'room__name')  # Ensure the `Room` model has a `name` field
    ordering = ('-created_at',)
    date_hierarchy = 'check_in_date'
    fieldsets = (
        (None, {
            'fields': ('room', 'full_name', 'number_of_persons')
        }),
        ('Booking Details', {
            'fields': ('check_in_date', 'check_out_date', 'special_requests')
        }),
        ('Payment Information', {
            'fields': ('payment_status',)
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at',)
