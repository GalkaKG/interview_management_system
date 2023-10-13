"""
ASGI config for interview_management_system project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter

from interview_management_system.interview_management.routing import ws_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'interview_management_system.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(URLRouter(ws_urlpatterns))
})


get_asgi_application()
