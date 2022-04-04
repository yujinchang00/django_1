from operator import mod
from django.db import models

# Create your models here.

class Index(models.Model) :
    name = models.CharField(max_length=200)
    menu = models.CharField(max_length=500)
    rate = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.name