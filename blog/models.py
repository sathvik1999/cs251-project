from django.db import models
from django.utils import timezone
from multiselectfield import MultiSelectField
#from django.contrib.postgres.fields import ArrayField


class Interest(models.Model):
    user=models.ForeignKey('auth.User',default=1)
    my_field = MultiSelectField(choices=(('fiction','fiction'),('fear','fear'),("fear1","fear1"),("fear2","fear2"),("fear3","fear3"),),default='fiction')
    published_date = models.DateTimeField(
            blank=True, null=True)
    
    
class Document(models.Model):
    genre_choices=(('fiction','fiction'),('fear','fear'),("fear1","fear1"),("fear2","fear2"),("fear3","fear3"),)

    user = models.ForeignKey('auth.User',default=1)
    title = models.CharField(max_length=200,default='')
    author = models.CharField(max_length=200,default='')
    genre = models.CharField(
        max_length=20,
        choices=genre_choices,
        default='fiction',)
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    image = models.ImageField(upload_to='images/',default = 'pic_folder/None/no-img.jpg')
    published_date = models.DateTimeField(auto_now_add=True)

class Rate(models.Model):
    user=models.ForeignKey('auth.User',default=1)
    doc=models.ForeignKey(Document)
    rating = models.IntegerField(choices=((1,1),(2,2),(3,3),(4,4),(5,5)),default=1)
    published_date = models.DateTimeField(blank=True, null=True)                                    
