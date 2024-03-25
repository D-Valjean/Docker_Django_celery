
from django.contrib import admin
from django.urls import path
from django.conf import settings
from notification.views import notification_page_view
from notification.consumers import NotificationConsumer

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", notification_page_view, name="notification_page")
]


websocket_urlpatterns = [
    path("ws/notifications/", NotificationConsumer.as_asgi())
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
