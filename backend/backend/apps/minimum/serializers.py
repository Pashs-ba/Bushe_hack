from rest_framework import serializers
from .models import Minimum


class MinimumSerializer(serializers.ModelSerializer):
    """Serializer for `Minimum` model (create)."""

    quarter = serializers.IntegerField(source="quarter.number")

    class Meta:
        model = Minimum
        fields = "__all__"
