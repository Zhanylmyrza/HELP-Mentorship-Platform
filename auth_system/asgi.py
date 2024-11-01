import os
import django
from django.core.asgi import get_asgi_application

# Set the default settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "auth_system.settings")

# Setup Django
django.setup()

# Import Channels routing components after Django is set up
from channels.routing import ProtocolTypeRouter, URLRouter
from chat.channels_middleware import JWTWebsocketMiddleware
from chat.routing import websocket_urlpatterns

# Get the ASGI application
django_asgi_app = get_asgi_application()

# Define the ASGI application with both HTTP and WebSocket routing
application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": JWTWebsocketMiddleware(URLRouter(websocket_urlpatterns)),
    }
)


# import os
# import django
# from django.core.asgi import get_asgi_application

# from channels.routing import ProtocolTypeRouter, URLRouter
# from chat.channels_middleware import JWTWebsocketMiddleware
# from chat.routing import websocket_urlpatterns


# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "auth_system.settings")

# django.setup()

# django_asgi_app = get_asgi_application()


# application = ProtocolTypeRouter(
#     {
#         "http": django_asgi_app,
#         "websocket": JWTWebsocketMiddleware(URLRouter(websocket_urlpatterns)),
#     }
# )
