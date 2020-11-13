from rest_framework.permissions import BasePermission

class IsDepartmentHead(BasePermission):

    message = "You must be an admin to access this page"

    def has_permission(self, request, view):

        user = request.user

        if user is not None and user.is_authenticated:
            return user.role == 'DH'

class IsEmployee(BasePermission):

    message = "You must be an admin to access this page"

    def has_permission(self, request, view):

        user = request.user

        if user is not None and user.is_authenticated:
            return user.role == 'EP'