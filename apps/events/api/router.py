from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from apps.events.api.viewset import RaceSeriesAPI, RaceAPI, ZwiftResultAPI

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("raceseries", RaceSeriesAPI)
router.register("races", RaceAPI)
router.register("zwift_result", ZwiftResultAPI)

urlpatterns = router.urls
