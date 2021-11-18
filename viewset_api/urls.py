from viewset_api.views import ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', ProductViewSet, basename='user')
urlpatterns = router.urls