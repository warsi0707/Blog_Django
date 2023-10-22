from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    caption = models.CharField(max_length=200)
    content = models.TextField()
    
    def __str__(self):
        return self.title


class contactUs(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    mobile= models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.name

class Comment(models.Model):
    name = models.CharField(max_length=100)
    text = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


    