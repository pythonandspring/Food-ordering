from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from customer import views as customerviews
from . import views

urlpatterns = [
    path('login/',customerviews.loginUser,name = 'login'),
    path('logout/',customerviews.logoutUser,name = 'logout'),
    path('register/',customerviews.registerUser,name = 'register'),
    path('forgetPassword/',customerviews.forgetPassword,name = 'forgetPassword'),
    path('feedback/', customerviews.feedback_form, name='feedback_form'),
    path('contact/', customerviews.index, name='index'),
    path('', customerviews.Home, name='Home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)