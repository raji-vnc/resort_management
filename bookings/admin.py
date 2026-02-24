from django.contrib import admin
from .models import Booking


admin.site.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer', 'room', 'check_in_date', 'check_out_date', 'status')
    list_filter = ('status', 'check_in_date', 'check_out_date')
    search_fields = ('customer__first_name', 'customer__last_name', 'room__room_number')

    
