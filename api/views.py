from django.shortcuts import render
from rest_framework.response import Response
from .models import Menulist
from rest_framework.views import APIView
from .serializers import MenulistSerializer

class MenuListAPI(APIView):
    def get(self, request):
        queryset = Menulist.objects.all()
        serializer = MenulistSerializer(queryset, many=True)
        return Response(serializer.data)