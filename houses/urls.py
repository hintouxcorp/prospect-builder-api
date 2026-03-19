from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import HouseViewSet, ContractViewSet, ContractItemViewSet, business_types

router = DefaultRouter()
router.register(r"houses", HouseViewSet, basename="house")
router.register(r"contracts", ContractViewSet, basename="contract")
router.register(r"contract-items", ContractItemViewSet, basename="contract-item")

urlpatterns = [
    path("business-types/", business_types),
]

urlpatterns += router.urls