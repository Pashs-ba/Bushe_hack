from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.PostsListCreateAPIView.as_view(), name="posts-list-create"),
    path("<str:slug>", views.PostsDetailAPIView.as_view(), name="posts-detail"),
]
