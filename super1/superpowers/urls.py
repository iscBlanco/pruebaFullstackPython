from rest_framework import routers
from .api import SuperPowersViewSet
 
router = routers.DefaultRouter()
router.register('api/superpowers', SuperPowersViewSet, 'superpowers')
 
urlpatterns = router.urls
