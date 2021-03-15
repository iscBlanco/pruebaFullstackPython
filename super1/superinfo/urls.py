from rest_framework import routers
from .api import SuperViewSet

router = routers.DefaultRouter()
router.register('api/super', SuperViewSet, 'leads')

urlpatterns = router.urls