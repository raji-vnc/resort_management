from django.urls import path,include
from rest_framework.routers import DefaultRouter    
from .views import BillingViewSet
router=DefaultRouter()
router.register(r'',BillingViewSet)

urlpatterns=[
    path('',include(router.urls)), 
    path('billing/',BillingViewSet.as_view({'get':'list','post':'create'}),name='billing-list'),
    path('billing/<int:pk>/',BillingViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'}),name='billing-detail'),
]