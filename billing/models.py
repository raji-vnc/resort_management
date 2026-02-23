from django.db import models

class Billing(models.Model):
    PAYMENT_STATUS=(
        ('Pending','pending'),
        ('Completed','completed'),
        ('Failed','failed'),
        ('Refunded','refunded')
    )
    customer=models.ForeignKey('customers.Customer',on_delete=models.CASCADE)
    booking=models.ForeignKey('bookings.Booking',on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    payment_method=models.CharField(max_length=50)
    room_charges=models.DecimalField(max_digits=10,decimal_places=2)
    service_charges=models.DecimalField(max_digits=10,decimal_places=2)
    tax_amount=models.DecimalField(max_digits=10,decimal_places=2)
    total_amount=models.DecimalField(max_digits=10,decimal_places=2)
    payment_status=models.CharField(max_length=20,choices=PAYMENT_STATUS,default='Pending')

    def total_amount(self):
        return self.room_charges + self.service_charges + self.tax_amount
        

    def __str__(self):
        return f"Billing for {self.customer} - {self.booking}"
    class Meta:
        verbose_name='Billing'
        verbose_name_plural='Billings'