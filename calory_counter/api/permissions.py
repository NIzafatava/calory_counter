from django.http import HttpRequest
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrCanUpdateDelete(BasePermission):
    def has_object_permission(self, request: HttpRequest, view, obj):
        if request.method in SAFE_METHODS or obj.user == request.user:
            return True

        if request.method in ["PUT", "PATCH"] and request.user.is_staff:
            return True

        if request.method in ["DELETE"] and request.user.is_staff:
            return True

        return False
