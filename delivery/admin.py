from django.contrib import admin
from delivery.models import deliveryUser

class DeliveryUserAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']

admin.site.register(deliveryUser, DeliveryUserAdmin)
