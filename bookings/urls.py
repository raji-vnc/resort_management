from django.urls import path
from .views import BookingViewSet

urlpatterns = [
    path('bookings/', BookingViewSet.as_view({'get': 'list', 'post': 'create'}), name='booking-list'),
    path('bookings/<int:pk>/', BookingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='booking-detail'),
    path('bookings/<int:pk>/check_in/', BookingViewSet.as_view({'post': 'check_in'}), name='booking-check-in'),
    path('bookings/<int:pk>/check_out/', BookingViewSet.as_view({'  post': 'check_out'}), name='booking-check-out'),
]