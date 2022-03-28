from django.urls import path
from . import main
from .tanium import taniumMain
from .ipu import ipuMain

urlpatterns = [
    path('', main.index),
    path('tanium/', taniumMain.index),
    path('ipu/', ipuMain.index),
]