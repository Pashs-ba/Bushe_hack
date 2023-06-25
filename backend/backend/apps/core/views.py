import time
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from .models import Order, Kitchen
from .serializers import *

# from backend.permissions import IsAdminPermission, IsDeliveryManPermission


class TestCeleryView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"test": "test"}, status=status.HTTP_200_OK)
    
class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # permission_classes = [IsAdminPermission | IsDeliveryManPermission]

    def update(self, request, *args, **kwargs):
        item = self.get_object()
        serializer = self.get_serializer(item, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



class KitchenViewSet(ModelViewSet):
    queryset = Kitchen.objects.all()
    serializer_class = KitchenSerializer
    # permission_classes = [IsAdminPermission | IsDeliveryManPermission]


