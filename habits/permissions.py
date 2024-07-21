from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_permission(self, request, view, obj):
        if obj.user == request.user:
            return True
        return False
