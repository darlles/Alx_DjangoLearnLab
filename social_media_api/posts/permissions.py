# posts/permissions.py
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    """
    Read-only for everyone; write actions only allowed for the resource owner.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        # obj may be Post or Comment; both have 'author'
        return getattr(obj, 'author', None) == request.user