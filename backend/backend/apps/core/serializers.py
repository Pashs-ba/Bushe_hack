from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet

from .models import Order, Kitchen, DeliveryMan


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ["order_id", "status", "order_list", "comments", "end_point", "actual_delivery_time",
                  "start_cook_time", "end_cook_time", "start_delivery_time", "end_delivery_time", "delivery_man_id"]


class KitchenSerializer(ModelSerializer):
    class Meta:
        model = Kitchen
        fields = ["point_id", "geotag"]


class DeliveryManSerializer(ModelSerializer):
    class Meta:
        model = DeliveryMan
        fields = ["delivery_man_id", "status"]
