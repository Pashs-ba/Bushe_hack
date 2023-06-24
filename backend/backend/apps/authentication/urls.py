from django.urls import path

from . import views

# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


app_name = "auth"

urlpatterns = [
    # path("users/", views.UserListAPIView.as_view(), name="users-list"),
    # path(
    #     "users/<int:pk>",
    #     views.UserRetrieveUpdateDeleteAPIView.as_view(),
    #     name="users-detail",
    # ),
    # path("users/delete", views.UserBulkDeleteAPIView.as_view(), name="users-delete"),
    path("users/create", views.CreateUserAPIView.as_view(), name="users-create"),

]
