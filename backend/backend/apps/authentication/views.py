import django_filters
import requests
from django.conf import settings
from django.urls import reverse
from rest_framework import generics, permissions, response, status, serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import (
    RefreshTokenSerializer,
    UserBulkDeleteSerializer,
    UserSerializer,
)
from .utils import ACCOUNT_TYPE_CHOICES, UserTypes, verify_telegram_authentication
from backend.permissions import IsAdminPermission


# TODO: Replace ActivateUserAPIView with frontend page

class ActivateUserAPIView(APIView):
    """Activate user account."""

    def get(self, request, uid, token):
        """Activate user account."""
        payload = {"uid": uid, "token": token}
        url = "{0}://{1}{2}".format(settings.PROTOCOL, settings.DOMAIN, reverse("user-activation"))
        response = requests.post(url, data=payload)
        if response.status_code == 204:
            return Response({"detail": "Account activated"}, status=status.HTTP_200_OK)
        return Response(response.json())


class ProfileView(generics.RetrieveAPIView):
    """Retrieve current user."""

    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Get current user."""
        return self.request.user


class UserListAPIView(generics.ListAPIView):
    """List users."""

    class UsersFilter(django_filters.FilterSet):
        account_type = django_filters.MultipleChoiceFilter(
            "account_type",
            choices=ACCOUNT_TYPE_CHOICES,
        )

        class Meta:
            model = User
            fields = []

    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_class = UsersFilter


class UserRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete a user."""

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserBulkDeleteAPIView(generics.DestroyAPIView):
    """
    Delete multiple users.

    Raises:
        Http403Forbidden: If the number of users to delete is greater than 50.
        Http400BadRequest: If the request data is invalid.

    Returns:
        Http204NoContent: If the users were deleted successfully.
    """

    serializer_class = UserBulkDeleteSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminPermission]

    def destroy(self, request, *args, **kwargs):
        """Delete multiple users."""
        serializer = UserBulkDeleteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        to_delete = list(map(int, request.data["ids"].split(",")))
        if len(to_delete) > settings.REST_FRAMEWORK["PAGE_SIZE"]:
            return response.Response(status=status.HTTP_403_FORBIDDEN)
        self.get_queryset().filter(id__in=to_delete).delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)


class LogoutView(APIView):
    """Logout users by blacklisting their refresh token."""

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        """Logout the user."""
        serializer = RefreshTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        refresh_token = serializer.validated_data["refresh"]
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception as e:
            raise TokenError(e)
        return Response(status=status.HTTP_205_RESET_CONTENT)


# TODO: CreateAdminAPIView


class CreateUserAPIView(generics.CreateAPIView):
    """API view for creating new users."""

    class CreateUserSerializer(serializers.ModelSerializer):
        hash = serializers.CharField()
        auth_date = serializers.IntegerField()
        id = serializers.IntegerField()

        class Meta:
            model = User
            fields = ["username", "first_name", "last_name",
                      "photo_url", "id", "auth_date", "hash"]
            extra_kwargs = {"hash": {"write_only": True}, "auth_date": {
                "write_only": True}, "id": {"write_only": True}}

        def validate(self, data):
            verify_telegram_authentication(data)
            return data

        def create(self, validated_data: dict):
            """Create a new student."""
            user = User.objects.create(
                account_type=UserTypes.COURIER.value,
                username=validated_data["username"],
                last_name=validated_data["last_name"],
                first_name=validated_data["first_name"],
                photo_url=validated_data["photo_url"],
                telegram_id=validated_data["id"]
            )
            user.set_password("")
            user.save()
            return user

    queryset = User.objects.all()
    serializer_class = CreateUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        instance_serializer = UserSerializer(instance)
        return Response(instance_serializer.data)
