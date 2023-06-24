from __future__ import annotations

from django.db import models
from django.utils.timezone import datetime
from backend.apps.authentication.models import User


from .utils import OrderStatus, ORDER_TYPE_CHOICES, DeliveryManStatus, DELIVERYMAN_TYPE_CHOICES

class Kitchen(models.Model):
    geotag = models.CharField(max_length=20)

    def __str__(self):
        return str(self.point_id)


class DeliveryMan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=DELIVERYMAN_TYPE_CHOICES, default=DeliveryManStatus.ready.value)
    def __str__(self):
        return str(self.user)


class Order(models.Model):
    status = models.IntegerField(choices=ORDER_TYPE_CHOICES, default=OrderStatus.opened.value)
    order_list = models.TextField() #TODO change to json
    comments = models.TextField(null=True,blank=True)  # comments from user
    delivery_comments = models.TextField(null=True,blank=True)
    end_point = models.CharField(max_length=200)  # address where to deliver
    kitchen_id = models.ForeignKey(Kitchen, on_delete=models.CASCADE)  # where to cook

    created_at = models.DateTimeField(auto_now_add=True, null=True,blank=True)  # when created
    expected_time = models.DateTimeField(null=True,blank=True)  # when to deliver
    end_delivery_time = models.DateTimeField(null=True,blank=True)  # when delivered

    # optional
    start_cook_time = models.DateTimeField(null=True,blank=True)
    end_cook_time = models.DateTimeField(null=True,blank=True)

    start_delivery_time = models.DateTimeField(null=True,blank=True)

    # hidden from user ?

    delivery_man_id = models.ForeignKey(DeliveryMan, on_delete=models.CASCADE, null=True,blank=True)
    number_in_queue = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return str(self.order_id)
