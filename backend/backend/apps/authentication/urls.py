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
    path("users/me", views.ProfileView.as_view(), name="current-user"),
    path("jwt/blacklist/", views.LogoutView.as_view(), name="logout"),
    path("users/create-student", views.CreateStudentAPIView.as_view(), name="create-student"),
    path("activate/<str:uid>/<str:token>/", views.ActivateUserAPIView.as_view()),
]
