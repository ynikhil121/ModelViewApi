from django.db import models

# Create your models here.
# myapp/models.py


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.CharField(max_length=255)
