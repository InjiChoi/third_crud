from django.shortcuts import render, redirect
from article.models import Article, Comment
from django.urls import reverse

# Create your views here.
def index(request):
    articles = Article.objects.all()
    ctx = {
        'articles':articles
    }
    return render(request, 'index.html', ctx)

def detail_article(request, pk):
    article = Article.objects.get(pk=pk)
    ctx = {
        'article':article
    }
    return render(request, 'detail.html', ctx)

def create_article(request):
    if request.method =='POST':
        print(request.POST)
        #원하는 키가 없으면 default로 None을 가져오겠다(더 안전한 방법)
        title = request.POST.get('title', None)
        content = request.POST.get('content', None)
        if title and content:
            article = Article.objects.create(
                title=title,
                content=content
            )
    return render(request, 'create.html')

def create_comment(request, pk):
    content = request.POST.get('comment', None)
    if content:
        article = Article.objects.get(pk=pk)
        comment = Comment.objects.create(
            article=article,
            # article_pk=pk,
            content=content
        )
    return redirect(reverse('detail_article', kwargs={'pk':pk}))