import time
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class TestCeleryView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"test": "test"}, status=status.HTTP_200_OK)
    
