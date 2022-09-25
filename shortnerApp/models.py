from django.db import models

# Create your models here.

class Linkk(models.Model):
    linkkk = models.CharField(max_length=100000)
    uuid = models.CharField(max_length=1000)
    