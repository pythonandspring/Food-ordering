from django.contrib import admin
from django.contrib import admin
from delivery.models import deliveryUser

class UserAdmin(admin.ModelAdmin):
    list_display = ['name','email','password']

admin.site.register(deliveryUser,UserAdmin)
