from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  CommentViewSet 
from customer.api.views import *
from delivery.api.views import DeliveryUserViewSet, FeedbackViewSet, ContactViewSet
from restaurant.api.views import *
from rest_framework.authtoken.views import obtain_auth_token
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="API for food ordering system",
        terms_of_service="https://www.google.com/policies/terms/",
        
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


router = DefaultRouter()
router.register(r'comments', CommentViewSet)
router.register(r'customer', CustomerViewSet)
router.register(r'feedback', FeedbackViewSet)
router.register(r'contact', ContactViewSet)
router.register(r'delivery-users', DeliveryUserViewSet)
router.register(r'feedbacks', FeedbackViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'restaurant',RestaurantViewSet)
router.register(r'payments',PaymentViewSet)
router.register(r'products',ProductViewSet)
router.register(r'carts',CartViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('token/', obtain_auth_token, name='api_token_auth'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),


]



