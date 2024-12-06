from django.contrib import admin
from order.models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ['item', 'quantity', 'sum_of_price', 'order_no', 'status', 'delivery_person', 'restaurant_name', 'comments', 'date_time']

admin.site.register(Order, OrderAdmin)