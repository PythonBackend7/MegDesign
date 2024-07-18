from django.db import models

# Create your models here.



class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Post(TimeStampedModel):
    title = models.CharField(max_length=100)
    body = models.TextField()
    def __str__(self):
        return self.title

class SocialMedia(TimeStampedModel):
    title = models.CharField(max_length=100)
    body = models.TextField()
    def __str__(self):
        return self.title

class Category(TimeStampedModel):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Subscribe(TimeStampedModel):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Author(TimeStampedModel):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()

    def __str__(self):
        return self.name

class PostImage(TimeStampedModel):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.title


