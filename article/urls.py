from article.views import *
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/', detail_article, name='detail_article'),
    path('create/', create_article, name='create_article'),
    path('comment/create/<int:pk>/',create_comment, name='create_comment'),
]