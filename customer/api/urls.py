from rest_framework.routers import DefaultRouter
from customer.api.views import CustomerUserViewSet

router = DefaultRouter()
router.register(r'customerusers', CustomerUserViewSet, basename='customeruser_unique3')  # Ensure basenames are unique

urlpatterns = router.urls
