from django.shortcuts import render
from rest_framework import viewsets
from .models import Billing
from .serializers import BillingSerializer 
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication 

class BillingViewSet(viewsets.ModelViewSet):
    queryset=Billing.objects.all()
    serializer_class=BillingSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]