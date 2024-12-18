from django.urls import path, include
from . import views

urlpatterns = [
    # path('api/', include(api_urls)),  # Include Delivery API URLs
    path('', views.home, name='home'),  # Ensure the home view is accessible
    # Add other delivery-specific URLs here if needed
]
