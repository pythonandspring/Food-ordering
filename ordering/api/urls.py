from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  CommentViewSet 
from customer.api.views import *
from delivery.api.views import *
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
        contact=openapi.Contact(email="contact@yourapi.local"), 
        license=openapi.License(name="BSD License"),       
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


router = DefaultRouter()
router.register(r'comments', CommentViewSet)
router.register(r'customer', CustomerViewSet)
router.register(r'contact', ContactViewSet)
router.register(r'delivery-persons', DeliveryPersonViewSet)
router.register(r'delivery-users', DeliveryUserViewSet)
router.register(r'feedback_delivery', Feedback_dViewSet ,basename='feedback_d')
router.register(r'contacts_delivery', Contact_dViewSet,basename='contacts_delivery')
router.register(r'restaurant',RestaurantViewSet)
router.register(r'payments',PaymentViewSet)
router.register(r'products',ProductViewSet)
router.register(r'carts',CartViewSet)
router.register(r'state',StateViewSet)
router.register(r'place',PlaceViewSet)
router.register(r'city',CityViewSet)
router.register(r'customerusers', CustomerUserViewSet, basename='customeruser_unique1')
router.register(r'restaurantusers', RestaurantUserViewSet)
router.register(r'foodItems', FoodItemsViewSet)
router.register(r'order', OrderViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('token/', obtain_auth_token, name='api_token_auth'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),


]



