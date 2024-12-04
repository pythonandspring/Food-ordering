# Add other delivery-specific URLs here if needed
from rest_framework.routers import DefaultRouter
from delivery.api.views import deliveryUserViewSet, FeedbackViewSet, ContactViewSet

# Create a router and register the viewsets
router = DefaultRouter()
router.register(r'delivery-users', deliveryUserViewSet, basename='deliveryuser')
router.register(r'feedbacks', FeedbackViewSet, basename='feedback')
router.register(r'contacts', ContactViewSet, basename='contact')

# Define the URL patterns
urlpatterns = router.urls
