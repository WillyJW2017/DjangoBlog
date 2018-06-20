from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def index(request):
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})

def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article':article})

def new_page(request, article_id):
    if str(article_id) == '0':
        return render(request, 'blog/new_article_page.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/new_article_page.html', {'article':article})

def new_action(request):
    title = request.POST.get('title', 'Default Title')
    content = request.POST.get('content', 'This is the default content')
    article_id = request.POST.get('ar_id', '0')
    if article_id == '0':
        models.Article.objects.create(Title=title, content=content)
        articles = models.Article.objects.all()
        return render(request, 'blog/index.html', {'articles': articles})
    article = models.Article.objects.get(pk=article_id)
    article.Title = title
    article.content = content
    article.save()
    return render(request, 'blog/article_page.html', {'article':article})