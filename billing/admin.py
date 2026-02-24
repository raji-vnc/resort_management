from django.contrib import admin

from .models import Billing

admin.site.register(Billing)
class BillingAdmin(admin.ModelAdmin):
    list_display = ('booking', 'amount', 'payment_status', 'payment_date')
    list_filter = ('payment_status', 'payment_date')
    search_fields = ('booking__customer__first_name', 'booking__customer__last_name', 'booking__room__room_number')

