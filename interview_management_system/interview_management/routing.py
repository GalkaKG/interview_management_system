from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from . import consumers

application = ProtocolTypeRouter({
    "websocket": URLRouter(
        [
            path("ws/feedback_reminder/", consumers.FeedbackReminderConsumer.as_asgi()),
            # Add more WebSocket paths and consumers as needed
        ]
    ),
})
