from backend.permissions import IsAdminPermission, IsAuthenticatedReadonlyPermission
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet

from .models import Quarter


class QuarterSerializer(ModelSerializer):
    """Serializer for `Quarter` model."""

    class Meta:
        model = Quarter
        fields = ["id", "number", "begin", "end"]


class QuarterViewSet(ModelViewSet):
    """ViewSet for `Quarter` model."""

    serializer_class = QuarterSerializer
    queryset = Quarter.objects.all()
    pagination_class = None
    permission_classes = [IsAuthenticatedReadonlyPermission | IsAdminPermission]
