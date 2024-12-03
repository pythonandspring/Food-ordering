from django.contrib import admin
from menu.models import Menu


class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'restaurant', 'availability', 'cost']

admin.site.register(Menu, MenuAdmin)