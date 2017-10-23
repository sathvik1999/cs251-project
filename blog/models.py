from django.db import models
from django.utils import timezone
from multiselectfield import MultiSelectField
from django.db.models.signals import post_save
from django.dispatch import receiver
#from django.contrib.postgres.fields import ArrayField

class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    picture=models.ImageField(upload_to='images/',default = 'pic_folder/None/no-img.jpg')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    
    #published_date = models.DateTimeField(blank=True, null=True)
    
class Interest(models.Model):
    user=models.OneToOneField('auth.User',default=1)
    my_field = MultiSelectField(choices=(('fiction','fiction'),('fear','fear'),("fear1","fear1"),("fear2","fear2"),("fear3","fear3"),),default='fiction')
    #published_date = models.DateTimeField(
     #       blank=True, null=True)
    
    
class Document(models.Model):
    genre_choices=(('fiction','fiction'),('fear','fear'),("fear1","fear1"),("fear2","fear2"),("fear3","fear3"),)
    rate1 = models.FloatField(null=True, blank=True, default=0.0)
    no_ratings = models.IntegerField(default=0)
    user=models.ForeignKey('auth.User',default=1)
    uploader = models.CharField(max_length=200,default='')
    title = models.CharField(max_length=200,default='')
    author = models.CharField(max_length=200,default='')
    genre = models.CharField(
        max_length=20,
        choices=genre_choices,
        default='fiction',)
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    image = models.ImageField(upload_to='images/',default = 'pic_folder/None/no-img.jpg')
    public = models.BooleanField(default=True)
    rmembers=models.ManyToManyField('auth.User',related_name='rmembers')
    published_date = models.DateTimeField(auto_now_add=True)
    searchshow = models.BooleanField(default=True)
    
    
class Rate(models.Model):
    user=models.ForeignKey('auth.User',default=1)
    doc=models.ForeignKey(Document)
    rating = models.IntegerField(choices=((1,1),(2,2),(3,3),(4,4),(5,5)),default=1)


class Follow(models.Model):
    user=models.OneToOneField('auth.User',default=1)
    flist=models.ManyToManyField('auth.User',related_name='owner1')

class Community(models.Model):
    admin=models.ForeignKey('auth.User',default=1)
    members=models.ManyToManyField('auth.User',related_name='members')
    name = models.CharField(max_length=200,default='')
    description = models.CharField(max_length=255, blank=True)
    documents=models.ManyToManyField('Document',related_name='docs')
    jrequests=models.ManyToManyField('auth.User',related_name='jrequests')

class Join(models.Model):
    user=models.ForeignKey('auth.User',default=1)
    jlist=models.ManyToManyField('Community',related_name='jlist')

class JoinPending(models.Model):
    com=models.ForeignKey('Community',default=1)
    jplist=models.ManyToManyField('auth.User',related_name='jplist')


class Advertise(models.Model):
    genre_choices=(('fiction','fiction'),('fear','fear'),("fear1","fear1"),("fear2","fear2"),("fear3","fear3"),)
    user=models.ForeignKey('auth.User',default=1)
    uploader = models.CharField(max_length=200,default='')
    title = models.CharField(max_length=200,default='')
    author = models.CharField(max_length=200,default='')
    genre = models.CharField(
        max_length=20,
        choices=genre_choices,
        default='fiction',)
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='images/',default = 'pic_folder/None/no-img.jpg')
    published_date = models.DateTimeField(auto_now_add=True)


class Readpending(models.Model):
    user=models.ForeignKey('auth.User',default=1)
    doc=models.ForeignKey(Document)
    rplist=models.ManyToManyField('auth.User',related_name='rplist')


    
