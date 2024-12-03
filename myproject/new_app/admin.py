from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from django.contrib import admin
from new_app.models import State, City, Place, UserLocation

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

class UserLocationAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'state', 'city', 'place')
    search_fields = ('user_name',)
    list_filter = ('state', 'city', 'place')

admin.site.register(State, StateAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(UserLocation, UserLocationAdmin)
