from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    message = "Only administrators can modify cinema data."

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return bool(
                request.user
                and request.user.is_authenticated
            )
        return bool(
            request.user
            and request.user.is_staff
        )
