from django.contrib import admin
from .models import User, Manager, DeliveryMan

admin.site.register(User)
admin.site.register(Manager)
admin.site.register(DeliveryMan)


