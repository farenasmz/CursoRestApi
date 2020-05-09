from django.urls import path
from rest_framework import routers
from .viewsets import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .views import ArticleView

from .models import Article
from . import views

route = routers.SimpleRouter()
route.register("element", ElementViewSet)
route.register("category", CategoryViewSet)
route.register("type", TypeViewSet)
urlpatterns = [
    path('articles/', ArticleView.as_view()),
]
