from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    """
    Admin interface for managing Payment records.
    """
    list_display = (
        'payment_id',
        'booking_id',
        'payer_id',
        'amount',
        'currency',
        'status',
        'description',
        'created_at',
    )
    search_fields = ('payment_id', 'payer_id', 'booking_id', 'description')  # Allow searching by Payment ID, Payer ID, Booking ID, and Description
    list_filter = ('status', 'currency', 'created_at')  # Filter payments by status, currency, and creation date
    ordering = ('-created_at',)  # Order payments by created_at in descending order
    date_hierarchy = 'created_at'  # Add date hierarchy for easier navigation by date

    # Add fieldsets for better organization in the detail view
    fieldsets = (
        ('Payment Details', {
            'fields': ('payment_id', 'booking_id', 'payer_id', 'amount', 'currency', 'status')
        }),
        ('Additional Information', {
            'fields': ('description', 'created_at'),
        }),
    )

    # Read-only fields for records that shouldn't be edited directly
    readonly_fields = ('created_at',)

    # Optionally customize the admin action buttons
    actions = ['mark_as_completed']

    def mark_as_completed(self, request, queryset):
        """
        Custom admin action to mark selected payments as 'Completed'.
        """
        updated_count = queryset.update(status='Completed')
        self.message_user(request, f"{updated_count} payments marked as Completed.")
    mark_as_completed.short_description = "Mark selected payments as Completed"
