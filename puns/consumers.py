import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Pun, Rating
from django.db.models import Avg

class RatingConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.pun_id = self.scope['url_route']['kwargs']['pun_id']
        self.room_group_name = f'pun_{self.pun_id}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        rating = data['rating']
        user = self.scope['user']

        await self.save_rating(self.pun_id, user, rating)
        new_avg_rating = await self.get_average_rating(self.pun_id)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'rating_update',
                'new_avg_rating': new_avg_rating,
                'pun_id': self.pun_id,
            }
        )

    async def rating_update(self, event):
        new_avg_rating = event['new_avg_rating']

        await self.send(text_data=json.dumps({
            'new_avg_rating': new_avg_rating
        }))

    @database_sync_to_async
    def save_rating(self, pun_id, user, rating):
        pun = Pun.objects.get(id=pun_id)
        Rating.objects.update_or_create(
            pun=pun, user=user, defaults={'rating': rating}
        )

    @database_sync_to_async
    def get_average_rating(self, pun_id):
        pun = Pun.objects.get(id=pun_id)
        return Rating.objects.filter(pun=pun).aggregate(Avg('rating'))['rating__avg'] or 0