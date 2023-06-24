import django_filters
from backend.apps.core.utils import MultipleValueFilter
from django.forms import IntegerField
from django.urls import path
from rest_framework import serializers, viewsets

from .models import Subject


class SubjectSerializer(serializers.ModelSerializer):
    """Serializer for `Subject` model."""

    class Meta:
        model = Subject
        fields = ("id", "name", "description", "icon")


class SubjectViewSet(viewsets.ModelViewSet):
    """Subject view set."""

    class SubjectFilter(django_filters.FilterSet):
        """Subject filter."""

        id = MultipleValueFilter(field_class=IntegerField)

        class Meta:
            model = Subject
            fields = ["name", "klass"]

    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    pagination_class = None
    filter_class = SubjectFilter


subject_list = SubjectViewSet.as_view({"get": "list", "post": "create"})

subject_detail = SubjectViewSet.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)

urlpatterns = [
    path("", subject_list, name="subject-list"),
    path("<int:pk>/", subject_detail, name="subject-detail"),
]
