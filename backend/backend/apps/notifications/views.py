import django_filters

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Notification
from .serializers import NotificationSerializer


class NotificationsList(ListCreateAPIView):
    """List all messages."""

    class NotificationFilter(django_filters.FilterSet):
        """Filter for notifications."""

        class Meta:
            """Meta class for filter."""

            model = Notification
            fields = ["user", "read", "category"]

    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    ordering = ["-created_at"]
    filter_class = NotificationFilter


class NotificationDetails(RetrieveUpdateDestroyAPIView):
    """Retrieve/update/destroy a message."""

    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class MarkAllNotificationsAsRead(APIView):
    """Mark all user's notifications as read."""

    def get(self, request):
        """Mark all notifications as read."""
        user = request.user
        Notification.objects.filter(user=user).update(read=True)
        return Response(status=200)
