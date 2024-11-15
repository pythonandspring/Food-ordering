from django.urls import path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet


router = DefaultRouter()
router.register(r'',CustomerViewSet)

urlpatterns = [
    path('api/',include(router.urls))
]