from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

class IsNotAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated :
            raise PermissionDenied(detail='You are already logged in G')
        return True
