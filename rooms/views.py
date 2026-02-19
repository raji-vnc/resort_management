from django.shortcuts import render
from rest_framework import viewsets
from .models import Room
from .serializers import RoomSerializer
from rest_framework.permissions import IsAuthenticated

class RoomViewSet(viewsets.ModelViewSet):
    queryset=Room.objects.all().order_by('room_number')
    serializer_class=RoomSerializer
    permission_classes = [IsAuthenticated]
