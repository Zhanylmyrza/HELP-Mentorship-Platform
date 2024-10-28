import os
import django
from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter
from chat.channels_middleware import JWTWebsocketMiddleware
from chat.routing import websocket_urlpatterns

django_asgi_app = get_asgi_application()


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "auth_system.settings")
django.setup()


application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": JWTWebsocketMiddleware(URLRouter(websocket_urlpatterns)),
    }
)
