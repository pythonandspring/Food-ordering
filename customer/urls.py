# from django.urls import path, include
# from .api import urls as api_urls


# urlpatterns = [
#     path('api/', include(api_urls)),
# ]
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from customer import views as customerviews
from . import views

urlpatterns = [
    
    path('login/',customerviews.loginUser,name = 'login'),
    path('logout/',customerviews.logoutUser,name = 'logout'),
    path('feedback/', customerviews.feedback_form, name='feedback_form'),
    path('contact/', customerviews.index, name='index'),
    path('', customerviews.Home, name='Home'),
    path('register/',customerviews.registerUser,name = 'register'),
    path('forgetPassword/',customerviews.forgetPassword,name = 'forgetPassword'),
    path('load-cities/', views.load_cities, name='load_cities'),
    path('load-places/', views.load_places, name='load_places'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
