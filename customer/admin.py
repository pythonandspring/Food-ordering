from django.contrib import admin
from .models import Customer, Order, Payment

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'address')
    search_fields = ('first_name', 'last_name', 'phone_number')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'total_amount', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at')
    search_fields = ('customer__first_name', 'customer__last_name')

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order', 'amount', 'payment_method', 'status', 'payment_date')
    list_filter = ('status', 'payment_date')
    search_fields = ('order__customer__first_name', 'order__customer__last_name')

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment, PaymentAdmin)
# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ('user', 'address', 'phone_number')
#     search_fields = ('user__username', 'phone_number')

# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('customer', 'status', 'created_at', 'updated_at')
#     list_filter = ('status', 'created_at')
#     search_fields = ('customer__user__username',)

# class PaymentAdmin(admin.ModelAdmin):
#     list_display = ('order', 'amount', 'payment_date')
#     list_filter = ('payment_date',)
#     search_fields = ('order__customer__user__username',)

# admin.site.register(Customer, CustomerAdmin)
# admin.site.register(Order, OrderAdmin)
# admin.site.register(Payment, PaymentAdmin)
