from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu_list, name='menu_list'),

    #Menus for a specific restaurant can be viewed on the restaurant_menus page.
    path('restaurant/<int:restaurant_id>/', views.restaurant_menus, name='restaurant_menus'),
    path('<int:pk>/', views.menu_detail, name='menu_detail'),
    path('add/', views.add_menu, name='add_menu'),
    path('<int:pk>/edit/', views.edit_menu, name='edit_menu'),
    path('<int:pk>/delete/', views.delete_menu, name='delete_menu'),
]
