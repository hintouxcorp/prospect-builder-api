from rest_framework import serializers
from .models import House, Contract, ContractItem, BusinessType

class BusinessTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessType
        fields = '__all__'

class HouseSerializer(serializers.ModelSerializer):

    # 🔥 declarar explicitamente
    custom_business = serializers.CharField(required=False, allow_null=True, allow_blank=True)

    class Meta:
        model = House
        fields = "__all__"
        read_only_fields = ["id", "owner", "created_at", "updated_at"]

    def create(self, validated_data):
        business_type = validated_data.get("business_type")
        custom_business = validated_data.get("custom_business")

        print("CREATE DEBUG:", business_type, custom_business)  # 🔍 debug

        if not business_type and custom_business:
            obj, created = BusinessType.objects.get_or_create(
                name=custom_business.strip()
            )
            validated_data["business_type"] = obj

        return super().create(validated_data)

    def update(self, instance, validated_data):
        business_type = validated_data.get("business_type")
        custom_business = validated_data.get("custom_business")

        print("UPDATE DEBUG:", business_type, custom_business)  # 🔍 debug

        if not business_type and custom_business:
            obj, created = BusinessType.objects.get_or_create(
                name=custom_business.strip()
            )
            validated_data["business_type"] = obj

        return super().update(instance, validated_data)

class ContractItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)
    unit_price = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = ContractItem
        fields = "__all__"

    def get_unit_price(self, obj):
        if obj.product.type == "product":
            return obj.product.price
        return obj.product.monthly_price

    def get_total_price(self, obj):
        return obj.total_price()


class ContractSerializer(serializers.ModelSerializer):
    items = ContractItemSerializer(many=True, read_only=True)
    client_name = serializers.ReadOnlyField(source="client.name")
    total_value = serializers.SerializerMethodField()

    class Meta:
        model = Contract
        fields = "__all__"
        read_only_fields = ["id", "owner", "created_at"]

    def get_total_value(self, obj):
        return obj.total_value()