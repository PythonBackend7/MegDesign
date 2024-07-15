from django.db import models


# Create your models here.
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Author(TimeStampedModel):
    name = models.CharField(max_length=212)
    image = models.ImageField(upload_to='images/')
    profession = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class Category(TimeStampedModel):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class Subscriber(TimeStampedModel):
    email = models.EmailField()

    def __str__(self):
        return self.email


class Social_Media(TimeStampedModel):
    title = models.CharField(max_length=212)
    link = models.URLField()

    def __str__(self):
        return self.title


class Extra_Images(TimeStampedModel):
    image = models.ImageField(upload_to='images/')


class Post(TimeStampedModel):
    title = models.CharField(max_length=212)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subscribers = models.ManyToManyField(Subscriber)
    social_media = models.ManyToManyField(Social_Media)
    extra_images = models.ManyToManyField(Extra_Images)

    def __str__(self):
        return self.title
