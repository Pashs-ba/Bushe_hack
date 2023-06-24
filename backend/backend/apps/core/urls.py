from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import TestCeleryView

router = SimpleRouter(trailing_slash=False)

urlpatterns = [
    # path("", include("backend.apps.core.config")),
    path("", include(router.urls)),
    path("test", TestCeleryView.as_view(), name="test"),
]
