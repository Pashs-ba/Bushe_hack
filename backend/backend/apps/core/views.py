import time
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from .models import Order, Kitchen, DeliveryMan
from .serializers import *


class TestCeleryView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"test": "test"}, status=status.HTTP_200_OK)
    
class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class KitchenViewSet(ModelViewSet):
    queryset = Kitchen.objects.all()
    serializer_class = KitchenSerializer

class DeliveryManViewSet(ModelViewSet):
    queryset = DeliveryMan.objects.all()
    serializer_class = DeliveryManSerializer