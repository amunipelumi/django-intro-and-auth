from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import HttpResponse
from . models import Article

def home(request):
    # return HttpResponse('Hello World')
    articles = Article.objects.all()
    context = {'articles':articles}
    return render(request, 'lynx/index.html', context)

def one_article(request, pk):
    article = Article.objects.get(id=pk)
    context = {'article':article}
    return render(request, 'lynx/article.html', context) 

def logout_view(request):
    logout(request)
    return redirect('home')