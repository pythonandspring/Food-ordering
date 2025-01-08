from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from customer import views as customerviews
from . import views

urlpatterns = [
    path('login/', customerviews.loginUser, name='login'),
    path('logout/', customerviews.logoutUser, name='logout'),
    path('contact/', customerviews.index, name='index'),
    path('', customerviews.Home, name='Home'),
    path('register/', customerviews.registerUser, name='register'),  # Ensure correct view is used
    path('forgetPassword/', customerviews.forgetPassword, name='forgetPassword'),
    path('load-cities/', customerviews.load_cities, name='load_cities'),
    path('load-places/', customerviews.load_places, name='load_places'),
    path('orders/', customerviews.orders, name='orders'),
    path('make_payment/', customerviews.make_payment, name='make_payment'),
    path('track_locations/<int:order_id>/', views.track_locations, name='track_locations'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
