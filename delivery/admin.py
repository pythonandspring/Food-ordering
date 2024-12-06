from django.contrib import admin
from delivery.models import deliveryUser

class DeliveryUserAdmin(admin.ModelAdmin):
    list_display = ['name', 'active_status', 'location']

admin.site.register(deliveryUser, DeliveryUserAdmin)
