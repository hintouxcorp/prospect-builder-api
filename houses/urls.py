from rest_framework.routers import DefaultRouter
from .views import (
    HouseViewSet,
    ContractViewSet,
    ContractItemViewSet,
    BusinessTypeViewSet
)

router = DefaultRouter()
router.register(r"houses", HouseViewSet, basename="house")
router.register(r"contracts", ContractViewSet, basename="contract")
router.register(r"contract-items", ContractItemViewSet, basename="contract-item")
router.register(r"business-types", BusinessTypeViewSet, basename="business-type")

urlpatterns = router.urls