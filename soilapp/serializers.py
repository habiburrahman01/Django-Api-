from .Models.models import soil
from rest_framework import serializers

class SoilSerializer(serializers.ModelSerializer):
    class Meta:
        model = soil
        fields=['ID','Name','ImagePath']

