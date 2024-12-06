from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderingViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'orderings', OrderingViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
