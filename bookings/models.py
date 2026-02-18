from django.db import models
from customers.models import Customer
from rooms.models import Room

class Booking(models.Model):

    BOOKING_STATUS=(
       ('Checked In','checked_in'),
       ('Checked Out','checked_out'),
       ('Cancelled','cancelled'),
       ('Reserved','reserved'),
       ('No Show','no_show'),
       ('Pending','pending'),
       ('Confirmed','confirmed')
    )
    
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    check_in_date=models.DateField()
    check_out_date=models.DateField()
    booking_status=models.CharField(max_length=20,choices=BOOKING_STATUS,default='Pending')
    total_price=models.DecimalField(max_digits=10,decimal_places=2)


    def __str__(self):
        return f"Booking for {self.customer} in room {self.room}"

    class Meta:
        verbose_name='Booking'
        verbose_name_plural='Bookings'

