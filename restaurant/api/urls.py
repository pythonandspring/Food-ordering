from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RestaurantViewSet ,ProductViewSet,PaymentViewSet,CartViewSet


router = DefaultRouter()
router.register(r'restaurant',RestaurantViewSet)
router.register(r'payments',PaymentViewSet)
router.register(r'products',ProductViewSet)
router.register(r'carts',CartViewSet)

urlpatterns = router.urls
