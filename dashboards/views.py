from django.shortcuts import render
from rest_framework.decorators import api_view
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


@api_view(['GET'])
def dashboard(request):

    total_rooms = Room.objects.count()
    available_rooms = Room.objects.filter(status="available").count()
    occupied_rooms = Room.objects.filter(status="occupied").count()

    total_bookings = Booking.objects.count()
    customers_count = Customer.objects.count()

    total_revenue = Billing.objects.filter(
        payment_status="paid"
    ).aggregate(Sum('total_amount'))['total_amount__sum'] or 0

    data = {
        "total_rooms": total_rooms,
        "available_rooms": available_rooms,
        "occupied_rooms": occupied_rooms,
        "total_bookings": total_bookings,
        "total_revenue": total_revenue,
        "customers_count": customers_count,
    }

    return Response(data)
