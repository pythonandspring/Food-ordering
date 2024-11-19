from django.urls import path, include
from .api import urls as api_urls

urlpatterns = [
    path('api/', include(api_urls)),  # Include Delivery API URLs
    # Add other delivery-specific URLs here if needed
]
