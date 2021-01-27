from rest_framework import routers
from .api import ShortenerViewSet

router = routers.DefaultRouter()
router.register('shortener', ShortenerViewSet, 'shortener')

urlpatterns = router.urls
