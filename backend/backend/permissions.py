from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

from backend.apps.authentication.utils import UserTypes


class IsAdminPermission(BasePermission):
    """Allows access only to admin users."""

    def has_permission(self, request, view):
        """Check if the user is an admin."""
        return request.user.account_type in (0, 1)


class IsStudentPermission(BasePermission):
    """Allows access only to students."""

    def has_permission(self, request, view):
        """Check if the user is a student."""
        return request.user.account_type == UserTypes.STUDENT.value


class IsMonitorStudentPermission(BasePermission):
    """Allows access only to monitor students."""

    def has_permission(self, request, view):
        """Check if the user is a monitor student."""
        return (
            request.user.account_type == UserTypes.STUDENT.value
            and request.user.options_student.is_monitor
        )


class StudentInKlassPermission(BasePermission):
    """Allows access only to students."""

    def has_permission(self, request, view):
        """Check if the user is a student."""
        print("Klass:", request.user.klass)
        return request.user.account_type == UserTypes.STUDENT.value and request.user.klass


class IsAuthenticatedReadonlyPermission(IsAuthenticated):
    """Allows access only to authenticated users if request method is safe."""

    def has_permission(self, request, view):
        if request.method not in SAFE_METHODS:
            return False
        return super().has_permission(request, view)
