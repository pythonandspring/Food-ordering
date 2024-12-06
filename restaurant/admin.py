from django.contrib import admin
from restaurant.models import restaurantUser, Restaurant, foodItems
# Register your models here.

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['restaurantName','address','restaurantContact','email','password']

admin.site.register(restaurantUser,RestaurantAdmin)


class FoodItemsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'image', 'restaurantName']

admin.site.register(Restaurant)
admin.site.register(foodItems, FoodItemsAdmin)
