from rest_framework import serializers
from .models import ProductSale

class ProductSaleSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductSale
        fields = "__all__"
