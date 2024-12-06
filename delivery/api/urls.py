from rest_framework.routers import DefaultRouter
from .views import DeliveryPersonViewSet

router = DefaultRouter()
router.register(r'delivery-persons', DeliveryPersonViewSet)

urlpatterns = router.urls