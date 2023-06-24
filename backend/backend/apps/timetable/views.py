from backend.apps.core.models import Klass
from backend.permissions import (
    IsAdminPermission,
    IsAuthenticatedReadonlyPermission,
    IsMonitorStudentPermission,
    IsStudentPermission,
    IsAuthenticated,
)
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.response import Response

from .models import Bell, TimetableLesson
from .serializers import (
    BellSerializer,
    CreateLessonsSerializer,
    DeleteLessonSerializer,
    LessonSerializer,
)


class BulkCreateLessonsAPIView(CreateAPIView):
    """Create multiple lessons."""

    serializer_class = CreateLessonsSerializer
    permission_classes = [IsAdminPermission | IsMonitorStudentPermission]

    def create(self, request):
        """Create multiple timetable records."""
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({"status": "ok"}, status.HTTP_201_CREATED)


class TimetableAPIView(ListCreateAPIView):
    """List lessons for a specified class or edit the timetable."""

    pagination_class = None
    serializer_class = LessonSerializer
    permission_classes = [IsStudentPermission | IsAdminPermission]

    def get_queryset(self):
        """Return timetable for klass."""
        klass = get_object_or_404(Klass, id=self.kwargs["pk"])
        return TimetableLesson.objects.filter(klass=klass)


class BulkDeleteLessonsAPIView(DestroyAPIView):
    """Delete multiple lessons."""

    queryset = TimetableLesson.objects.all()
    serializer_class = DeleteLessonSerializer
    permission_classes = [IsAdminPermission | IsMonitorStudentPermission]

    def destroy(self, request, *args, **kwargs):
        """Delete multiple lessons."""
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        to_delete = []
        for lesson in serializer.validated_data:
            try:
                lsn = TimetableLesson.objects.get(
                    number__n=lesson["n"],
                    day=lesson["day"],
                    klass=lesson["klass"],
                    subject=lesson["subject"],
                )
                to_delete.append(lsn.id)
            except TimetableLesson.DoesNotExist:
                pass
        TimetableLesson.objects.filter(id__in=to_delete).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListBellsAPIView(ListAPIView):
    """List bells."""

    permission_classes = [IsAuthenticated | IsAdminPermission | IsMonitorStudentPermission]
    serializer_class = BellSerializer
    queryset = Bell.objects.all()


class BellAPIView(RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete a bell."""

    permission_classes = [
        IsAuthenticatedReadonlyPermission | IsAdminPermission | IsMonitorStudentPermission
    ]
    queryset = Bell.objects.all()
    serializer_class = BellSerializer
