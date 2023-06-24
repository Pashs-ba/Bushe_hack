from django.urls import path

from .views import MarkAllNotificationsAsRead, NotificationDetails, NotificationsList

app_name = "notifications"

urlpatterns = [
    path("", NotificationsList.as_view(), name="list"),
    path("<int:pk>/", NotificationDetails.as_view(), name="details"),
    path("mark-all-as-read/", MarkAllNotificationsAsRead.as_view(), name="mark-all-as-read"),
]
