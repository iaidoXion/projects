from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Menulist
from rest_framework.views import APIView
from .serializers import MenulistSerializer
from .tests import check_air

def index(request):
    res = check_air()
    pm10 = res.get('다사읍')
    context = {'station': '다사읍', 'pm10': pm10}
    print(context)
    return render(request, 'home.html', context)

class MenuListAPI(APIView):
    def get(self, request):
        queryset = Menulist.objects.all()
        #print(queryset)
        serializer = MenulistSerializer(queryset, many=True)
        return Response(serializer.data)


