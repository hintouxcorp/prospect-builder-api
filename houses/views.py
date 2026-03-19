from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import House, Contract, ContractItem, BusinessType
from .serializers import HouseSerializer, BusinessTypeSerializer, ContractSerializer, ContractItemSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import mixins, viewsets, generics

class BusinessTypeListCreateView(generics.ListCreateAPIView):
    queryset = BusinessType.objects.all()
    serializer_class = BusinessTypeSerializer

class BusinessTypeViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    queryset = BusinessType.objects.all().order_by("created_at")
    serializer_class = BusinessTypeSerializer

@api_view(['GET'])
def business_types(request):
    types = House.objects.values_list('business_type', flat=True).distinct()

    result = []

    for t in types:
        label = dict(House.BUSINESS_CHOICES).get(t, t)

        result.append({
            "value": t,
            "label": label
        })

    return Response(result)

@method_decorator(csrf_exempt, name="dispatch")
class HouseViewSet(ModelViewSet):
    serializer_class = HouseSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = House.objects.all()

        business_type = self.request.query_params.get('business_type')

        if business_type:
            queryset = queryset.filter(business_type=business_type)

        return queryset

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

