from django.db import models
from project.models import TimeStampedModel

class Article(TimeStampedModel):
    title = models.CharField(max_length=255, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    
class Comment(TimeStampedModel):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    # related_name x => default : article.comment_set
    content = models.CharField(max_length=255, verbose_name='댓글')

"""
1:n Foreignkey
1:1 OneToOneField
n:m ManyToManyField
"""