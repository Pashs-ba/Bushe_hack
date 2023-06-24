from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView


urlpatterns = [
    path("admin-extended/", admin.site.urls),
    path("api/blog/", include("backend.apps.blog.urls")),
    path("api/notifications/", include("backend.apps.notifications.urls")),
    path("api/timetable/", include("backend.apps.timetable.urls")),
    path("api/", include("backend.apps.homework.urls")),
    path("api/", include("backend.apps.core.urls")),
    path("api/", include("backend.apps.minimum.urls")),
    # Djoser & SimpleJWT
    path("api/auth/", include("backend.apps.authentication.urls")),
    path("api/auth/", include("djoser.urls")),
    path("api/auth/", include("djoser.urls.jwt")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    index_view = never_cache(TemplateView.as_view(template_name="index.html"))
    urlpatterns += [path("", index_view, name="index")]
