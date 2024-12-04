from rest_framework.routers import DefaultRouter
from delivery.api.views import DeliveryUserViewSet, FeedbackViewSet, ContactViewSet

router = DefaultRouter()
router.register(r'delivery-users', DeliveryUserViewSet)
router.register(r'feedbacks', FeedbackViewSet)
router.register(r'contacts', ContactViewSet)

urlpatterns = router.urls
