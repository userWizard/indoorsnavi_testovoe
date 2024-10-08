from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from src.cats.models.cats import CatsModel
from src.api.v1.cats.shemas.cats import (
    CatsSerializer,
    CreateCatsSerializer
)
from src.api.v1.permissions import OwnerOrReadOnly

class CatsViewSet(viewsets.ModelViewSet):
    '''ViewSet for cats.'''
    queryset = CatsModel.objects.all()
    serializer_class = CreateCatsSerializer()
    pagination_class = PageNumberPagination
    permission_classes = (OwnerOrReadOnly,)
    
    
    def get_serializer_class(self):
        if self.action == 'create':
            return CreateCatsSerializer
        return CatsSerializer
