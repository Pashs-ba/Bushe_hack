from django.urls import include, path
from rest_framework.routers import SimpleRouter

router = SimpleRouter(trailing_slash=False)

urlpatterns = [
    path("", include("backend.apps.core.config")),
    path("", include(router.urls)),
]
