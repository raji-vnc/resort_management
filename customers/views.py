from django.shortcuts import render
from rest_framework import viewsets
from .models import Customer    
from .serializers import CustomerSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter



class CustomerViewSet(viewsets.ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer
    permission_classes=[IsAuthenticated]
    filter_backends=[SearchFilter]
    search_fields=['first_name','last_name','email','phone_number','username','place','id_proof_number','id_prrof_type','gender']



