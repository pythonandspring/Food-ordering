from rest_framework.routers import DefaultRouter
from customer.api.views import CustomerUserViewSet, AdditionalViewSet

router = DefaultRouter()
router.register(r'customerusers', CustomerUserViewSet, basename='customeruser_unique3')  # Ensure basenames are unique
router.register(r'additional', AdditionalViewSet, basename='additional_unique4')

urlpatterns = router.urls
