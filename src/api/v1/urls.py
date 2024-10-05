from django.urls import path, include
from rest_framework.routers import DefaultRouter

from src.api.v1.users.handlers.users import UserViewSet

router_v1 = DefaultRouter()

router_v1.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router_v1.urls)),
]
