from django.db import models

# Create your models here.
# myapp/models.py


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.CharField(max_length=255)

# # myapp/serializers.py
# from rest_framework import serializers
# from .models import Article

# class ArticleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = ['id', 'title', 'body', 'author']

# # myapp/views.py
# from django.shortcuts import render
# from rest_framework import viewsets
# from .models import Article
# from .serializers import ArticleSerializer

# class ArticleViewSet(viewsets.ModelViewSet):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# # myapp/urls.py
# from django.urls import path, include
# from rest_framework import routers
# from . import views

# router = routers.DefaultRouter()
# router.register('articles', views.ArticleViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]
