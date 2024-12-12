from django.contrib import admin
from delivery.models import deliveryUser

class DeliveryUserAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'deliveryContact']

admin.site.register(deliveryUser, DeliveryUserAdmin)
