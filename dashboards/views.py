from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action    
from rest_framework.permissions import IsAuthenticated
from billing.models import Billing
from bookings.models import Booking
from customers.models import Customer
from rooms.models import Room
from .models import Dashboard
from .serializers import DashboardSerializer
from django.db.models import Count, Sum
from rest_framework.permissions import AllowAny



@api_view(['GET'])
def dashboard(request):

    print("Rooms:", Room.objects.count())
    print("Bookings:", Booking.objects.count())
    print("Total Revenue:", Billing.objects.aggregate(total_revenue=Sum('amount'))['total_revenue'])
    print("Total Customers:", Customer.objects.count())

    return Response({
        "rooms": Room.objects.count(),
        "bookings": Booking.objects.count(),
        "total_revenue": Billing.objects.aggregate(total_revenue=Sum('amount'))['total_revenue'] or 0,
        "customers": Customer.objects.count()
    })