from rest_framework.permissions import BasePermission

class IsValidUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.user == obj.user
        )

class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.user.id == obj.user.id
        )