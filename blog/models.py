from django.db import models
from django.utils import timezone
#from django.contrib.postgres.fields import ArrayField

class Post(models.Model):
    fiction='fi'
    fear='fe'
    genre_choices=(
        (fiction,'fiction'),
        (fear,'fear'))
    uploader = models.ForeignKey('auth.User',default=1)
    title = models.CharField(max_length=200,default='')
    text = models.TextField(default="")
    genre = models.CharField(
        max_length=2,
        choices=genre_choices,
        default=fiction,)
    #created_date = models.DateTimeField(
     #       default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    author = models.CharField(max_length=200,default="")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Interest(models.Model):
    user=models.ForeignKey('auth.User',default=1)
    genre = models.CharField(max_length=200,default='')
    published_date = models.DateTimeField(
            blank=True, null=True)
    
    
