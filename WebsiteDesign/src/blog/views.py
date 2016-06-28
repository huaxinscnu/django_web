from django.http.response import Http404
from django.shortcuts import render, redirect

from blog.models import Article


# Create your views here.
def base(request):
    return render(request,'nourl.html')

def welcome(request):
    return render(request,'welcome.html')

def article_list(request):
    articles = __get_no_hidden_articles()
    return render(request,'article_list.html',{'articles':articles})

def __get_no_hidden_articles():
    articles = []  # 获取全部的Article对象
    for article_list in Article.objects.all():
        if not article_list.hidden:
            articles.append(article_list)
    return articles

def __get_a_no_hidden_article(id):
    try:
        detail = Article.objects.get(id=id)
    except Article.DoesNotExist:
        return Article.objects
    
    if not detail.hidden:
        return detail
    
    
def article_detail(request,id):
    detail = __get_a_no_hidden_article(id)
    if not detail:
        return render(request,'article_no_found.html')
    return render(request,'article_detail.html',{'article':detail})

def article_new(request):
    return render(request,'article_new.html')

def about_me(request):
    return render(request, 'about_me.html')

def search_tag(request, tag) :
    try:
        post_list = Article.objects.filter(category__iexact = tag) #contains
    except Article.DoesNotExist :
        return render(request,'article_no_found.html')
    
    return render(request, 'archives.html', {'post_list' : post_list})

def search_author(request,author):
    try:
        post_list = Article.objects.filter(article_author__iexact = author) #contains
    except Article.DoesNotExist :
        return render(request,'article_no_found.html')
    return render(request, 'archives.html', {'post_list' : post_list})
    
def blog_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request,'base.html')
        else:
            post_list = Article.objects.filter(title__icontains = s)
            if len(post_list) == 0 :
                return render(request,'archives.html', {'post_list' : post_list,
                                                    'error' : True})
            else :
                return render(request,'archives.html', {'post_list' : post_list,
                                                    'error' : False})
    return redirect('/')

def page_not_found(request):
    return render(request,'Error/404.html')

def page_error(request):
    return render(request,'Error/500.html')
