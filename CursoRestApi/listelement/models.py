from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length = 255)
    url_clean = models.CharField(max_length = 255)

    def __str__(self):
        return self.title

class Type(models.Model):
    title = models.CharField(max_length = 255)
    url_clean = models.CharField(max_length = 255)

    def __str__(self):
        return self.title

class Element(models.Model):
    title = models.CharField(max_length = 255)
    url_clean = models.CharField(max_length = 255)
    url_clean = models.TextField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    type = models.ForeignKey(Type, on_delete = models.CASCADE)

    def __str__(self):
        return self.title


class Author(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField()

class Article(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    body = models.TextField()