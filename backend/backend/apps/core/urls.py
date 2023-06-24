from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import TestCeleryView, OrderViewSet, KitchenViewSet, DeliveryManViewSet


router = SimpleRouter(trailing_slash=False)
router.register("orders", OrderViewSet)
router.register("kitchens", KitchenViewSet)
router.register("delivery_man_id", DeliveryManViewSet)

urlpatterns = [
    # path("", include("backend.apps.core.config")),
    path("", include(router.urls)),
    path("test", TestCeleryView.as_view(), name="test"),
]
