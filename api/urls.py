from django.urls import path
from .views import MenuListAPI

app_name = 'api'

urlpatterns = [
    path('menuList/', MenuListAPI.as_view()),
]