from rest_framework.routers import DefaultRouter
from .views import ProductSaleViewSet

router = DefaultRouter()
router.register(r"sales", ProductSaleViewSet)

urlpatterns = router.urls
