from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from customer import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('feedback/', views.feedback_form, name='feedback_form'),
    path('contact/', views.index, name='index'),
    path('', views.Home, name='Home'),  # Ensure home view is defined
    path('register/', views.registerUser, name='register'),
    path('forgetPassword/', views.forgetPassword, name='forgetPassword'),
    path('load-cities/', views.load_cities, name='load_cities'),
    path('load-places/', views.load_places, name='load_places'),
    path('orders/', views.orders, name='orders'),
    path('make_payment/', views.make_payment, name='make_payment'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
