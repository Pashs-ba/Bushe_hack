from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

from backend.apps.authentication.utils import UserTypes


class IsManagerPermission(BasePermission):
    def has_permission(self, request, view):
        """Check if the user is a manager."""
        return request.user.account_type == UserTypes.MANAGER.value


class IsDeliveryManPermission(BasePermission):
    def has_permission(self, request, view):
        """Check if the user is a delivery man."""
        return request.user.account_type == UserTypes.COURIER.value


class IsAuthenticatedReadonlyPermission(IsAuthenticated):
    """Allows access only to authenticated users if request method is safe."""

    def has_permission(self, request, view):
        if request.method not in SAFE_METHODS:
            return False
        return super().has_permission(request, view)
