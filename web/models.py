from django.db import models

# Create your models here.

class MenuSetting(models.Model):
    menuId = models.CharField(max_length=50)
    menuName = models.CharField(max_length=200)
    menuUrl = models.CharField(max_length=200)
    menuImg = models.CharField(max_length=200)
    menuUse = models.CharField(max_length=10)
    menuNote = models.TextField()
    menuCreateDate = models.DateTimeField()


