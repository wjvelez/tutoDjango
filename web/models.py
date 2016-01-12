from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Diagrama(models.Model):
    nombre = models.CharField(max_length = 20)
