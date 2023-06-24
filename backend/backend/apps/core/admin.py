from django.contrib import admin

from .models import Order, Kitchen, DeliveryMan

admin.site.register(Order)
admin.site.register(Kitchen)
admin.site.register(DeliveryMan)

