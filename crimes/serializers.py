from rest_framework import serializers
from .models import CrimePoint

class CrimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrimePoint
        fields = "__all__"
