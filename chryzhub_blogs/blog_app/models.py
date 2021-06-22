from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=225)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog_detail', args=(str(self.id)))

    def get_absolute_url(self,*args,**kwargs):
        return reverse('blog_detail',kwargs={'pk': self.pk})

class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete = models.CASCADE)
    bio = models.TextField()

    def __str__ (self):
        return str(self.user)

class Post(models.Model):
    title = models.CharField(max_length=225)
    header_image = models.ImageField(blank= True, null=True, upload_to='images')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField()
    #body = models.TextField()
    post_date = models.DateField(auto_now_add = True)
    category = models.CharField(max_length=225, default='coding')
    snippet = models.CharField(max_length=225)
    likes = models.ManyToManyField(User, related_name='blog_post')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('blog_detail', args=(str(self.id)))

    def get_absolute_url(self,*args,**kwargs):
        return reverse('blog_detail',kwargs={'pk': self.pk})
