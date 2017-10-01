from django.db import models
from django.utils import timezone


class Post(models.Model):
    fiction='fi'
    fear='fe'
    de=1
    genre_choices=(
        (fiction,'fiction'),
        (fear,'fear'))
    uploader = models.ForeignKey('auth.User',default=de)
    title = models.CharField(max_length=200)
    text = models.TextField()
    genre = models.CharField(
        max_length=2,
        choices=genre_choices,
        default=fiction,)
    #created_date = models.DateTimeField(
     #       default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    author = models.CharField(max_length=200)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title