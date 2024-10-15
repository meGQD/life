from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied
from django.contrib import messages

class IsNotLoggedIn(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            raise PermissionDenied(detail='You are not logged in')
        return True