from rest_framework.viewsets import ModelViewSet
from .models import ProductSale
from .serializers import ProductSaleSerializer

class ProductSaleViewSet(ModelViewSet):
    queryset = ProductSale.objects.all()
    serializer_class = ProductSaleSerializer
