from rest_framework import serializers
from .models import Menulist

class MenulistSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Menulist  # product 모델 사용
        fields = '__all__'  # 모든 필드 포함