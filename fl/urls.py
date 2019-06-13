
from rest_framework.routers import DefaultRouter

from fl.views import PageViewSet

router = DefaultRouter()
router.register('api/pages', PageViewSet)


urlpatterns = router.urls