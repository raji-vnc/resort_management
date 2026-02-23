from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet

router=DefaultRouter()
router.register(r'',CustomerViewSet)        
urlpatterns=[
    path('',include(router.urls)) ,
    path('customers/',CustomerViewSet.as_view({'get':'list','post':'create'}),name='customer-list'),
    path('customers/<int:pk>/',CustomerViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'}),name='customer-detail'),
]