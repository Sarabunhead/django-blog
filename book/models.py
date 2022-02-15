from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

def __str__(self):
    return self.name

def get_absolute_url(self):
    return reverse('list')



class post(models.Model) :
    author =models.ForeignKey(User, on_delete=models.CASCADE,related_name="blog_posts")
    slug =models.SlugField(max_length=250,unique_for_date="publish")
    publish =models.DateTimeField(default=timezone.now)
    title =models.CharField(max_length=250)
    title_tag = models.CharField(max_length=250, default="this is my blog")
    body = RichTextField(blank = True, null = True)
    # body =models.TextField()
    created =models.DateTimeField(auto_now_add=True)
    upadated =models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=255, default='coding')
    likes = models.ManyToManyField(User, related_name='blog_postd')

    def total_likes(self):
        return self.likes.count()
    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        # return reverse("article-ditail", args = (str(self.id)))
        return reverse('list')