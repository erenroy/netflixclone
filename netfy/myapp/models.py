from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORY_CHOICES = (
    ('All' , 'Everything'),
    ('A' , 'Anime'),
    ('H' , 'Hollywood'),
    ('K' , 'korean Drama'),
    ('AC' , 'Action'),
    ('S' , 'sad'),
    ('M' , 'Mature'),
)

class Video(models.Model):
    title = models.CharField(max_length=100)
    desc =  models.TextField()
    date = models.DateField(auto_now=False,auto_now_add=False)
    small_image = models.ImageField(upload_to='images')
    big_image = models.ImageField(upload_to='bigimages')
    video_file = models.FileField(upload_to='video')
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=25,default='All')
    slug = models.CharField(max_length=130)

    def __str__(self):
        return str(self.id)

class Comment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class UserDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_age = models.IntegerField(default=15)
    user_name = models.CharField(max_length=100)
    user_choice = models.CharField(max_length=30,default='All')
    user_image = models.ImageField(upload_to='profileimages')
   

class Catogory_movie(models.Model):
    title = models.CharField(max_length=100)
    small_image = models.ImageField(upload_to='movie_images')
    slug = models.CharField(max_length=130)

class Catogory_anime(models.Model):
    title = models.CharField(max_length=100)
    small_image = models.ImageField(upload_to='animme_images')
    slug = models.CharField(max_length=130)

class Catogory_new_release(models.Model):
    title = models.CharField(max_length=100)
    small_image = models.ImageField(upload_to='new_images')
    slug = models.CharField(max_length=130)

class Cart(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    movie = models.ForeignKey(Video,on_delete=models.CASCADE)


# Building the user interaction section 
