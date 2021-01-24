from rest_framework.permissions import BasePermission


class isCreator(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class isCreatorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return True
        return obj.user == request.user
