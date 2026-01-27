"""
ASGI config for quickstart project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

django_app = get_asgi_application()

# Now we can import other apps and channels
from cms_mcp.asgi import mcp_app


async def application(scope, receive, send):
    """Route HTTP requests based on path."""

    if scope['type'] == 'http' and scope.get('path') == '/mcp/' or scope['type'] == 'lifespan':
        return await mcp_app(scope, receive, send)
    # All other requests go to Django
    return await django_app(scope, receive, send)

