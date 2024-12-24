from django.contrib import admin
from customer.models import customerUser, Contact, Order, State, City, Place
from import_export.admin import ImportExportModelAdmin

class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'state', 'city', 'place', 'address']  # Ensure 'address' is displayed
    search_fields = ('name', 'email', 'address')  # Add 'address' to search fields
    list_filter = ('state', 'city', 'place')

admin.site.register(customerUser, UserAdmin)

class Comments(admin.ModelAdmin):
    list_display = ['stars', 'comments']


admin.site.register(Contact)

class StateAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

class CityAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'state')
    list_filter = ('state',)
    search_fields = ('name',)

class PlaceAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'city')
    list_filter = ('city',)
    search_fields = ('name',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_no', 'customer', 'item', 'quantity', 'sum_of_price', 'status', 'restaurant_name', 'delivery_person', 'date_time']  # Add 'delivery_person'
    search_fields = ('order_no', 'customer__name', 'restaurant_name', 'delivery_person')  # Add 'delivery_person'
    list_filter = ('status', 'restaurant_name', 'date_time', 'delivery_person')  # Add 'delivery_person'

admin.site.register(Order, OrderAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Place, PlaceAdmin)
