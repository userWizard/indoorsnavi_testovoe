from rest_framework.permissions import SAFE_METHODS, BasePermission

class OwnerOrReadOnly(BasePermission):
  '''Custom permission for owners only. Or read-only.'''

  def has_object_permission(self, request, view, obj):

    if request.method in SAFE_METHODS:
      return True
    
    return obj.owner == request.user

  def has_permission(self, request, view):
    return request.user.is_authenticated or request.method in SAFE_METHODS
