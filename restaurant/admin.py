from django.contrib import admin
from restaurant.models import restaurantUser, foodItems
# from restaurant.models import State, City, Place, UserLocation  # Ensure this import is correct

# Register your models here.

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['restaurantName', 'address', 'restaurantContact', 'email', 'password']

admin.site.register(restaurantUser, RestaurantAdmin)

class FoodItemsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'image', 'category', 'restaurantName']  # Add 'category'

# admin.site.register(Restaurant)
admin.site.register(foodItems, FoodItemsAdmin)

from import_export.admin import ImportExportModelAdmin

# class StateAdmin(ImportExportModelAdmin):
#     list_display = ('id', 'name')
#     search_fields = ('name',)

# class CityAdmin(ImportExportModelAdmin):
#     list_display = ('id', 'name', 'state')
#     list_filter = ('state',)
#     search_fields = ('name',)

# class PlaceAdmin(ImportExportModelAdmin):
#     list_display = ('id', 'name', 'city')
#     list_filter = ('city',)
#     search_fields = ('name',)

# class UserLocationAdmin(admin.ModelAdmin):
#     list_display = ('user_name', 'state', 'city', 'place')
#     search_fields = ('user_name',)
#     list_filter = ('state', 'city', 'place')

# admin.site.register(State, StateAdmin)
# admin.site.register(City, CityAdmin)
# admin.site.register(Place, PlaceAdmin)
# admin.site.register(UserLocation, UserLocationAdmin)
