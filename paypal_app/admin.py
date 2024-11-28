# admin.py
from django.contrib import admin
from .models import Payment

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_id', 'payer_id', 'amount', 'currency', 'status', 'description', 'created_at')
    search_fields = ('payment_id', 'payer_id', 'description')
    list_filter = ('status', 'currency')
    ordering = ('-created_at',)

    # You can add more customization if needed, like fieldsets, actions, etc.
    # fieldsets = (
    #     (None, {
    #         'fields': ('payment_id', 'payer_id', 'amount', 'currency', 'status', 'description')
    #     }),
    # )

admin.site.register(Payment, PaymentAdmin)
