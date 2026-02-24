from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.db.models import Count, Sum
from billing.models import Billing
from bookings.models import Booking
from customers.models import Customer
from rooms.models import Room

class DashboardViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def list(self, request):
        total_bookings = Booking.objects.count()
        total_customers = Customer.objects.count()
        total_rooms = Room.objects.count()
        total_revenue = Billing.objects.aggregate(
            total=Sum('total_amount')
        )['total'] or 0

        return Response({
            "total_bookings": total_bookings,
            "total_customers": total_customers,
            "total_rooms": total_rooms,
            "total_revenue": total_revenue
        })