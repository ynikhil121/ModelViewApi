from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('articles', views.ArticleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]