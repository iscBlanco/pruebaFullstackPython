from rest_framework import routers
from .api import SuperViewSet

router = routers.DefaultRouter()
router.register('api/super', SuperViewSet, 'superinfo')

urlpatterns = router.urls