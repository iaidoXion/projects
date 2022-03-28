from django.urls import path
from . import main
from .tanium import taniumMain
from .ipu import ipuMain

app_name = 'xion'

urlpatterns = [
    path('', main.index),
    path('tanium/', taniumMain.index, name='index'),
    path('ipu/', ipuMain.index),
    path('xion/<int:question_id>/', main.detail, name='detail'),
path('answer/create/<int:question_id>/', main.answer_create, name='answer_create'),
]