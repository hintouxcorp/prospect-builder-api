from rest_framework.routers import DefaultRouter
from .views import CrimeViewSet

router = DefaultRouter()
router.register("crimes", CrimeViewSet)

urlpatterns = router.urls
