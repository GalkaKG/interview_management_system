import asyncio
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async


class FeedbackReminderConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        user = self.scope['user']
        if user.is_authenticated:
            await self.send(json.dumps({'message': 'You are connected.'}))
        else:
            await self.close()

    async def disconnect(self, close_code):
        pass

    async def notify_feedback_needed(self, event):
        await self.send(json.dumps({'message': 'Feedback is needed for the interview.'}))
