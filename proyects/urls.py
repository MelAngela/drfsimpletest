from rest_framework import routers
from .api import ProyectViewSet

router = routers.DefaultRouter()

router.register('api/projects', ProyectViewSet, 'projects')

urlpatterns = router.urls