from django.db import models

# Create your models here.

class Diagrama(models.Model):
    nombre = models.CharField(max_length = 20)
