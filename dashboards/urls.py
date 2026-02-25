from rest_framework.routers import DefaultRouter
from .views import DashboardViewSet
from django.urls import path, include

urlpatterns =[
    path('api/dashboard/', DashboardViewSet.as_view({'get': 'get'}), name='dashboard'),

]