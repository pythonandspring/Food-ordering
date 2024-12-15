from django.contrib import admin
from customer.models import customerUser, Feedback, Contact, Order
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from django.contrib import admin
from customer.models import State, City, Place

class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'password', 'state', 'city', 'place']
    search_fields = ('name',)
    list_filter = ('state', 'city', 'place')

admin.site.register(customerUser, UserAdmin)
# Register your models here.
class Comments(admin.ModelAdmin):
    list_display = ['stars', 'comments']

admin.site.register(Feedback, Comments)
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
    list_display = ['order_no', 'customer', 'item', 'quantity', 'sum_of_price', 'status', 'restaurant_name', 'date_time']
    search_fields = ('order_no', 'customer__name', 'restaurant_name')
    list_filter = ('status', 'restaurant_name', 'date_time')

admin.site.register(Order, OrderAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Place, PlaceAdmin)
