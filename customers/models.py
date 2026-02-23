import django
from django.db import models
from django.utils import timezone

class Customer(models.Model):
    GENDER_CHOICES=(
        ('Male','male'),        
        ('Female','female'),
        ('Other','other')
    )
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=20)    
    gender=models.CharField(max_length=10,choices=GENDER_CHOICES,default=True)
    username=models.CharField(max_length=50,unique=True)
    password=models.CharField(max_length=128)
    id_prrof_type=models.CharField(max_length=50,default=True)
    id_proof_number=models.CharField(max_length=50,default=True)
    place=models.CharField(max_length=100)

  
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name='Customer'
        verbose_name_plural='Customers'