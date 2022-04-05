from django.db import models

class Menulist(models.Model):
    menuId = models.CharField(max_length=50)
    menuName = models.CharField(max_length=200)
    menuCreateDate = models.DateTimeField()
    menuUse = models.CharField(max_length=10)
    menuNote = models.TextField()

    def __str__(self):
        return self.menuName