from django.urls import path, include
from .api import urls as api_urls
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from restaurant import views as restaurantviews
from . import views

urlpatterns = [

    path('logoutRestaurant/',restaurantviews.logoutRestaurant,name = 'logoutR'),
    path('loginRestaurant/',restaurantviews.loginRestaurant,name = 'loginRestaurant'),
    path('registerRestaurant/',restaurantviews.registerRestaurant,name = 'registerRestaurant'),
    path('addMenu/', restaurantviews.addMenu, name='addMenu'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns = [
#     path('api/', include(api_urls)),  # Include Restaurant API URLs
#     # Add other restaurant-specific URLs here if needed
# ]
