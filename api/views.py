from rest_framework.response import Response
from .models import Menulist
from rest_framework.views import APIView
from .serializers import MenulistSerializer

class MenuListAPI(APIView):
    def get(self, request):
        queryset = Menulist.objects.all()
        print(queryset)
        serializer = MenulistSerializer(queryset, many=True)
        return Response(serializer.data)
