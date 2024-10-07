from django.contrib import admin
from .models import (
    Order,
    Coupon,
    OrderedProduct,
)


@admin.register(OrderedProduct)
class OrderedProductModelAdmin(admin.ModelAdmin):
    list_display = ['product', 'size', 'color', 'quantity']


@admin.register(Order)
class OrderModelAmin(admin.ModelAdmin):
    list_display = ['date', 'total_price', 'delivered']
    list_filter = ['date', 'delivered']


@admin.register(Coupon)
class CouponModelAdmin(admin.ModelAdmin):
    list_display = ['code', 'limitation', 'discount_percentage']
    list_filter = [ 'discount_percentage',]
    search_fields = ['code', ]

