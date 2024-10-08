from django.urls import path

from src.consumers.chats import ChatConsumer

ws_urlpatterns = [
    path('ws/api/v1/', ChatConsumer.as_asgi()),
]