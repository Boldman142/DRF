from rest_framework.permissions import BasePermission


class Moderator(BasePermission):

    def has_permission(self, request, view):
        if request.user.groups.filter(name='модераторы учебы').exists():
            return request.method not in ['CREATE', 'DELETE']
        # if request.user.is_superuser:
        #     return True
        return False


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return request.method in ['GET', 'PUT', 'PATCH', 'DELETE']
        return False

