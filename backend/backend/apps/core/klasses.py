from rest_framework.serializers import ModelSerializer

from .models import Klass
from django.urls import path
import django_filters
from rest_framework.generics import ListAPIView, RetrieveAPIView


class KlassSerializer(ModelSerializer):
    """Serializer for `Klass` model.

    Fields: `name`, `students`, `teachers`,
    `head_teacher`, `description`, `subjects`

    """

    class Meta:
        model = Klass
        fields = "__all__"


class KlassCompactSerializer(ModelSerializer):
    """Serializer for `Klass` model.

    Fields: `id`, `name`, `head_teacher`, `description`
    """

    class Meta:
        model = Klass
        fields = ["id", "name", "head_teacher", "description"]


class KlassListAPIView(ListAPIView):
    """List all `Klass` instances."""

    class KlassFilter(django_filters.FilterSet):
        """Filter for `Klass` instances."""

        class Meta:
            model = Klass
            fields = []

    serializer_class = KlassSerializer
    queryset = Klass.objects.all()
    ordering = ["name"]
    # filter_class = KlassFilter
    pagination_class = None

    def get_serializer(self, *args, **kwargs):
        """Return compact serializer."""
        if self.request.query_params.get("compact", "False").lower() == "true":
            self.serializer_class = KlassCompactSerializer
        return super().get_serializer(*args, **kwargs)


class KlassRetrieveAPIView(RetrieveAPIView):
    """Retrieve a single `Klass` instance."""

    serializer_class = KlassSerializer
    queryset = Klass.objects.all()


urlpatterns = [
    path("", KlassListAPIView.as_view(), name="klass-list"),
    path("<int:pk>", KlassRetrieveAPIView.as_view(), name="klass-detail"),
]
