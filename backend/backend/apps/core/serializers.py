from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet

from .models import Order, Kitchen, DeliveryMan



class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ["__all__"]


class KitchenSerializer(ModelSerializer):
    class Meta:
        model = Kitchen
        fields = ["geotag"]


class DeliveryManSerializer(ModelSerializer):
    class Meta:
        model = DeliveryMan
        fields = ["user", "status"]
