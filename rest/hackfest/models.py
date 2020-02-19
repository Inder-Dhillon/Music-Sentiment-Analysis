from django.db import models

# Create your models here.


class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500,blank=True,null=True) 
    artist = models.CharField(max_length=100,blank=True,null=True) 
    lyric = models.CharField(max_length=1000,blank=True,null=True) 
    category = models.CharField(max_length=500,blank=True,null=True) 
    sentiment = models.CharField(max_length=100,blank=True,null=True) 
    magnitude = models.CharField(max_length=100,blank=True,null=True) 
    
    
    
    
    
