from django.urls import path

from . import views

app_name = "homework"

urlpatterns = [
    path("homework", views.HomeworkListCreateAPIView.as_view()),
    path("homework/<int:pk>", views.HomeworkDetailAPIView.as_view()),
    path("homework/dates", views.ListHomeworkDatesAPIView.as_view()),
    path(
        "homework/<int:hw_pk>/attachments",
        views.AttachmentsListCreateAPIView.as_view(),
    ),
    path(
        "homework/<int:hw_pk>/attachments/<int:pk>",
        views.AttachmentsDetailAPIView.as_view(),
    ),
]
