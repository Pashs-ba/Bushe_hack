from rest_framework import viewsets
import django_filters
from .models import Minimum
from .serializers import MinimumSerializer


class MinimumViewSet(viewsets.ModelViewSet):
    """ViewSet for Minimum model."""

    class ProductFilter(django_filters.FilterSet):
        class Meta:
            model = Minimum
            fields = ["subject", "grade", "quarter__number"]

    serializer_class = MinimumSerializer
    queryset = Minimum.objects.all()
    filter_class = ProductFilter
