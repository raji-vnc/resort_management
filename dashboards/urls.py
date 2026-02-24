
from django.urls import path
from .views import dashboard

urlpatterns = [
    path('dashboards/',dashboard, name='dashboard-overview'),

]