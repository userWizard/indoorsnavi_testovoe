from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination

from src.api.v1.users.shemas.users import (
    UserCreateSerializer,
    UserSerializer,
)
from src.users.models.users import UserModel


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

