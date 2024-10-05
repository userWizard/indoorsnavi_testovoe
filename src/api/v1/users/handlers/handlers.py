from rest_framework.viesets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions

from src.api.v1.users.shemas.users import UserCreateSerializer, UserSerializer
from src.users.models.users import UserModel
from src.api.v1.permissions import AuthorOrReadOnly


class UserViewSet(ModelViewSet):
    '''ViewSet for users.'''
    queryset = UserModel.objects.all()
    serializer_class = UserCreateSerializer()
    pagination_class = PageNumberPagination
    permissions_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        return UserSerializer

    def get_permissions(self):
        if (self.request.method == 'POST'
           and self.request.path == '/api/v1/users/'):
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [AuthorOrReadOnly]
        return [permission() for permission in permission_classes]
