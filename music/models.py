from django.db import models

# Create your models here.
class Album(models.model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

class Song(models.model):
    album = models.name = models.ForeignKeyField('Album', related_name='', on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)