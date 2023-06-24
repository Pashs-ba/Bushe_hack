import django_filters
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet

from .models import Group


class GroupSerializer(serializers.ModelSerializer):
    """Serializer for `Group` model."""

    class Meta:
        model = Group
        fields = ["id", "subject", "klass", "students"]


class GroupViewSet(ModelViewSet):
    """ViewSet for `Quarter` model."""

    class GroupFilter(django_filters.FilterSet):
        class Meta:
            model = Group
            fields = ["klass"]

    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    pagination_class = None
