from django.urls import path
from . import views

urlpatterns = [
    path('restaurants/', views.filter_restaurants, name='filter_restaurants'),
    path('restaurant/<int:restaurant_id>/', views.menu_views, name='menuviews'),
]
