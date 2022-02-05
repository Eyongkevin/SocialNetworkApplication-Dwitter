from django.db import models

# Create your models here.
class Solo(models.Model):
    track = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    instrument = models.CharField(max_length=50)