from rest_framework import serializers
from sorl_thumbnail_serializer.fields import HyperlinkedSorlImageField

from backend.apps.authentication.serializers import CompactUserSerializer

from .models import Posts


class PostSerializer(serializers.ModelSerializer):
    """Serializer for `Posts` model (list & retrieve)."""

    author = CompactUserSerializer(read_only=True)

    thumbnail = HyperlinkedSorlImageField(
        "128x128", options={"crop": "center"}, source="image", read_only=True
    )

    class Meta:
        model = Posts
        fields = "__all__"


class PostCreateSerializer(serializers.ModelSerializer):
    """Serializer for `Posts` model (create)."""

    class Meta:
        model = Posts
        fields = "__all__"
