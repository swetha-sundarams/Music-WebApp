from django.db import models
from django.contrib.auth.models import User
import datetime
import os
def getFileName(request,file_name):
    nt=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_file_name="%s%s"%(nt,file_name)
    return os.path.join('uploads/',new_file_name)# Create your models here.

class category(models.Model):
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=getFileName,null=True,blank=True)
    #audio_file = models.FileField(upload_to='audio/')
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show|1-Hidden")
    Created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class songs(models.Model):
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    name=models.CharField(max_length=150,null=False,blank=False)
    category_name=models.CharField(max_length=150,null=False,blank=False)
    Singer=models.CharField(max_length=150,null=False,blank=False)
    writer=models.CharField(max_length=150,null=False,blank=False)
    music=models.CharField(max_length=150,null=False,blank=False)
    song_image=models.ImageField(upload_to=getFileName,null=True,blank=True)
    audio_file = models.FileField(upload_to='audio/')
    movie_name=models.CharField(max_length=150,null=False,blank=False)
    language=models.CharField(max_length=150,null=False,blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show|1-Hidden")
    Trending=models.BooleanField(default=False,help_text="0-normal|1-trend")
    Created_at=models.DateTimeField(auto_now_add=True)

class Liked_song(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    song_like=models.ForeignKey(songs,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
class favorite(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    song_like=models.ForeignKey(songs,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)


