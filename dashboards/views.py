from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.db.models import Count, Sum
from billing.models import Billing
from bookings.models import Booking
from customers.models import Customer
from rooms.models import Room
from .models import Dashboard
from .serializers import DashboardSerializer
from rest_framework.decorators import action, permission_classes

@permission_classes([IsAuthenticated])
class DashboardViewSet(viewsets.ViewSet):
    def get(self,request):
        results = {
            'total_bookings': Booking.objects.count(), 
            'total_revenue': Billing.objects.aggregate(total_revenue=Sum('amount'))['total_revenue'] or 0,
            'total_customers': Customer.objects.count(),
            'total_rooms': Room.objects.count(),
        }
        return Response(results)