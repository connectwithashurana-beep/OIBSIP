from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from .health import health_check
from .serve_spa import SpaFallbackView

urlpatterns = [
    path("health/", health_check),
    path("admin/", admin.site.urls),
    path("api/auth/", include("accounts.urls")),
    path("api/inventory/", include("inventory.urls")),
    path("api/orders/", include("orders.urls")),
    path("api/payments/", include("payments.urls")),
    path("api/notifications/", include("notifications.urls")),
    path("api/dashboard/", include("dashboard.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve the built React app (SPA) for everything that isn't an API/admin path.
urlpatterns += [
    re_path(
        r"^(?!api/|admin/|media/|static/|health/)(?P<path>.*)$",
        SpaFallbackView.as_view(),
        name="spa",
    ),
]
