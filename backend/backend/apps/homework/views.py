import django_filters
from backend.apps.core.models import Klass
from django.db.models import Count, Q, QuerySet
from django.db.models.functions import Length
from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Homework, HomeworkAttachment
from .serializers import (
    AttachmentCreateSerializer,
    AttachmentSerializer,
    CreateHomeworkSerializer,
    HomeworkSerializer,
    UpdateHomeworkSerializer,
)


class HomeworkFilter(django_filters.FilterSet):
    has_content = django_filters.BooleanFilter(method="has_content_check")
    date = django_filters.DateFromToRangeFilter(field_name="lesson__date")
    klass = django_filters.ModelChoiceFilter(
        queryset=Klass.objects.all(), field_name="lesson__group__klass"
    )

    class Meta:
        model = Homework
        fields = ["date", "has_content"]

    def has_content_check(self, queryset: QuerySet[Homework], name, value):
        """Select homework that has attached files or content."""
        qs = queryset.annotate(content_len=Length("content"), files_cnt=Count("attachments"))
        filter_expr = Q(content_len__gt=0) | Q(files_cnt__gt=0)
        if value:
            return qs.filter(filter_expr)
        return qs.filter(~filter_expr)


class HomeworkListCreateAPIView(generics.ListCreateAPIView):
    """List homework API View."""

    class HomeworkPagination(PageNumberPagination):
        page_size = 50
        max_page_size = 100
        page_size_query_param = "page_size"

    queryset = Homework.objects.all()
    pagination_class = HomeworkPagination
    filter_class = HomeworkFilter
    ordering = ["lesson__date", "lesson__group__subject"]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreateHomeworkSerializer
        return HomeworkSerializer

    def perform_create(self, serializer):
        return serializer.save()

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        instance_serializer = HomeworkSerializer(instance)
        headers = self.get_success_headers(instance_serializer.data)
        return Response(instance_serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class HomeworkDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Homework.objects.all()

    def get_serializer_class(self):
        if self.request.method in ("PUT", "PATCH"):
            return UpdateHomeworkSerializer
        return HomeworkSerializer

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class AttachmentsListCreateAPIView(generics.ListCreateAPIView):
    pagination_class = None

    def get_serializer_class(self):
        if self.request.method == "POST":
            return AttachmentCreateSerializer
        return AttachmentSerializer

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs.setdefault("context", self.get_serializer_context())
        if serializer_class == AttachmentCreateSerializer:
            kwargs.setdefault("homework_id", self.kwargs["hw_pk"])
        return serializer_class(*args, **kwargs)

    def get_queryset(self):
        return HomeworkAttachment.objects.filter(homework_id=self.kwargs["hw_pk"])


class AttachmentsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AttachmentSerializer

    def get_queryset(self):
        return HomeworkAttachment.objects.filter(homework_id=self.kwargs["hw_pk"])

    def destroy(self, request, *args, **kwargs):
        """
        Destroy `HomeworkAttachment` instance.

        If the corresponding `Homework` instance has no other
        files or content attached to it, it also deletes the
        homework itself.
        """
        instance: HomeworkAttachment = self.get_object()
        hw_obj: Homework = instance.homework
        if not hw_obj.content and not hw_obj.files_attached:
            hw_obj.delete()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListHomeworkDatesAPIView(APIView):
    def get(self, request):
        qs = Homework.objects.all()
        filtered_data = HomeworkFilter(request.GET, qs).qs
        data = list(filtered_data.values_list("lesson__date", flat=True).distinct())
        return Response(data, status=status.HTTP_200_OK)
