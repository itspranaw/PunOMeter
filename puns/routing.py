from django.urls import path
from .consumers import RatingConsumer

websocket_urlpatterns = [
    path("ws/puns/<int:pun_id>/", RatingConsumer.as_asgi()),
]