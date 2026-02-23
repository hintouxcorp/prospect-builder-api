from rest_framework.routers import DefaultRouter
from .views import HouseViewSet
from .views import ContractViewSet, ContractItemViewSet

router = DefaultRouter()
router.register(r"houses", HouseViewSet, basename="house")
router.register(r"contracts", ContractViewSet, basename="contract")
router.register(r"contract-items", ContractItemViewSet, basename="contract-item")

urlpatterns = router.urls
