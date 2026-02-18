from django.shortcuts import render
from rest_framework import viewsets
from .models import Booking
from .serializers import BookingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response

class BookingViewSet(viewsets.ModelViewSet):
    queryset=Booking.objects.all()
    serializer_class=BookingSerializer

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    @action(detail=True, methods=['POST'])
    def check_in(self, request, pk=None):
        booking = self.get_object()
        if booking.status == 'booked':
            booking.status = 'checked_in'
            booking.save()
            return Response({'status': 'Checked in successfully'})
        else:
            return Response({'status': 'Invalid booking status for check-in'}, status=400)
        
    @action(detail=True, methods=['POST'])
    def check_out(self, request, pk=None):
        booking = self.get_object()
        if booking.status == 'checked_in':
            booking.status = 'checked_out'
            booking.save()
            return Response({'status': 'Checked out successfully'})
        else:
            return Response({'status': 'Invalid booking status for check-out'}, status=400)

