from django.db import models
from unittest.util import _MAX_LENGTH
from datetime import datetime

# Create your models here.
class Artiste (models.Model):
    Artiste_id = models.IntegerField(primary_key=True)
    Firstname = models.CharField(max_length = 20)
    Lastname = models.CharField(max_length = 20)
    Age = models.IntegerField

class Song (models.Model):
    Artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    Datereleased = models.DateField(default=datetime.today)
    Likes = models.CharField(max_length=1000)
    Song_id = models.IntegerField(primary_key=True)

class Lyric (models.Model):
    Content = models.CharField(max_length= 1000)
    Song_id = models.ForeignKey(Song, on_delete=models.CASCADE)