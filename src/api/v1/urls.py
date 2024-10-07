from django.urls import path, include
from rest_framework.routers import DefaultRouter

from src.api.v1.users.handlers.users import UserViewSet
from src.api.v1.cats.handlers.cats import CatsViewSet

router_v1 = DefaultRouter()

router_v1.register(r'users', UserViewSet, basename='users')
router_v1.register(r'cats', CatsViewSet, basename='cats')

urlpatterns = [
    path('', include(router_v1.urls)),
]
