from __future__ import annotations

from django.db import models
from django.utils.timezone import datetime
from authentication.models import User


from .utils import OrderStatus, ORDER_TYPE_CHOICES, DeliveryManStatus, DELIVERYMAN_TYPE_CHOICES
# Юзеры [user_id PK, $\dots$]
# Доставщики [delman_id PK, status (enum: ready, busy, at_home), ]
# Заказы [order_id PK, user_id FK, delman_id FK, status (enum: opened, cooking, on_the_way, closed), order_time, start_delivery_time, end_delivery_time, kitchen_id FK, end_point (geotag)]
# Точки - кухня [point_id PK, geotag]



class Kitchen(models.Model):
    point_id = models.AutoField(primary_key=True)
    geotag = models.CharField(max_length=20)

    def __str__(self):
        return self.point_id


class DeliveryMan(models.Model):
    delivery_man_id = models.ForeignKey(User, on_delete=models.SET_NULL)
    status = models.IntegerField(choices=DELIVERYMAN_TYPE_CHOICES, default=DeliveryManStatus.ready.value)

    def __str__(self):
        return self.delivery_man_id


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    status = models.IntegerField(choices=ORDER_TYPE_CHOICES, default=OrderStatus.opened.value)
    order_list = models.JSONField()
    comments = models.TextField()  # comments from user

    end_point = models.CharField(max_length=20)  # address where to deliver
    kitchen_id = models.ForeignKey(Kitchen, on_delete=models.SET_NULL)  # where to cook

    created_at = models.DateTimeField(auto_now_add=True)  # when created
    expected_time = models.DateTimeField()  # when to deliver
    actual_delivery_time = models.DateTimeField()  # when delivered

    # optional
    start_cook_time = models.DateTimeField()
    end_cook_time = models.DateTimeField()

    start_delivery_time = models.DateTimeField()
    end_delivery_time = models.DateTimeField()

    # hidden from user ?

    delivery_man_id = models.ForeignKey(DeliveryMan, on_delete=models.SET_NULL)

    def __str__(self):
        return self.order_id
