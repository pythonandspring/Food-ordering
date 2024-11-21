from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderingViewSet, CommentViewSet
from customer.api.views import *
from restaurant.api.views import *
from delivery.api.views import *

router = DefaultRouter()
router.register(r'orderings', OrderingViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'delivery-persons', DeliveryPersonViewSet)
router.register(r'customer',CustomerViewSet)
router.register(r'restaurant',RestaurantViewSet)
router.register(r'payments',PaymentViewSet)
router.register(r'products',ProductViewSet)
router.register(r'carts',CartViewSet)



urlpatterns = [
    path('', include(router.urls)),
]
