from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.views.static import serve

from django.conf import settings  # for deployement via AWS, to see the css statis etc.
from django.conf.urls.static import (
    static,
)  # for deployement via AWS, to see the css statis etc.

urlpatterns = [
    path("auth/", include("djoser.urls.jwt")),
    path("auth/", include("djoser.urls")),
    path("person/", include("accounts.urls")),
    path("media/<path:path>", serve, kwargs={"document_root": settings.MEDIA_ROOT}),
    path("chat/", include("chat.urls")),
]


urlpatterns += [re_path(r"^.*", TemplateView.as_view(template_name="index.html"))]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
