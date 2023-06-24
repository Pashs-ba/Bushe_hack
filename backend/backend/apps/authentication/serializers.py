from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    """Serializer for `User` model."""

    class Meta:
        model = models.User
        fields = [
            "account_type", "first_name", "last_name",
            "username", "id", "photo_url", "is_active",
            "last_login", "date_joined", "is_admin"
        ]

        read_only_fields = [
            "id", "account_type", "is_active", "username"
        ]


class UserBulkDeleteSerializer(serializers.Serializer):
    ids = serializers.CharField()


class RefreshTokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()
