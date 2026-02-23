from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import House
from .serializers import HouseSerializer
from .models import Contract, ContractItem
from .serializers import ContractSerializer, ContractItemSerializer

@method_decorator(csrf_exempt, name="dispatch")
class HouseViewSet(ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(owner=self.request.user)
        else:
            serializer.save()

@method_decorator(csrf_exempt, name="dispatch")
class ContractViewSet(ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(owner=self.request.user)
        else:
            serializer.save()


@method_decorator(csrf_exempt, name="dispatch")
class ContractItemViewSet(ModelViewSet):
    queryset = ContractItem.objects.all()
    serializer_class = ContractItemSerializer
    permission_classes = [AllowAny]

