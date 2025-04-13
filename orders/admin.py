from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import (
    Customer, Order, OrderItem,
    Drink, DrinkType, Flavor, Milk,
    Pastry, PastryType, Merch
)

class OrderItemInline(GenericTabularInline):
    model = OrderItem
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'customer', 'created_at', 'is_complete')
    inlines = [OrderItemInline]

# Register your models here.
admin.site.register(Customer)
admin.site.register(Drink)
admin.site.register(DrinkType)
admin.site.register(Flavor)
admin.site.register(Milk)
admin.site.register(Pastry)
admin.site.register(PastryType)
admin.site.register(Merch)

admin.site.register(Order, OrderAdmin)

admin.site.register(OrderItem)