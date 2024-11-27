from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'booking',
        'amount',
        'status',
        'payment_id',
        'created_at',
    )
    list_filter = ('status', 'created_at')
    search_fields = ('booking__full_name', 'payment_id')  
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    fieldsets = (
        (None, {
            'fields': ('booking', 'amount')
        }),
        ('Payment Details', {
            'fields': ('status', 'payment_id')
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at', 'payment_id')
