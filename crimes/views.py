from rest_framework.viewsets import ModelViewSet
from .models import CrimePoint
from .serializers import CrimeSerializer

class CrimeViewSet(ModelViewSet):
    queryset = CrimePoint.objects.all()
    serializer_class = CrimeSerializer
