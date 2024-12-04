from rest_framework.routers import DefaultRouter
from ordering.api.views import CommentViewSet

router = DefaultRouter()
router.register(r'comments', CommentViewSet)

urlpatterns = router.urls

