from django.db import models

class Room(models.Model):
    ROOM_TYPE=(
        ('Single','single'),
        ('Double','double'),
        ('Suite','suite'),
    )
    ROOM_STATUS=(
        ('Available','available'),
        ('Occupied','occupied'),
    )
    room_number=models.CharField(max_length=10,unique=True)
    room_type=models.CharField(max_length=10,choices=ROOM_TYPE,default='Single')
    room_status=models.CharField(max_length=10,choices=ROOM_STATUS,default='Available')
    price=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.room_number

    class Meta:
        verbose_name='Room'
        verbose_name_plural='Rooms' 
        

