from .views import MinimumViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter(trailing_slash=False)
router.register("minimums", MinimumViewSet)
urlpatterns = router.urls
