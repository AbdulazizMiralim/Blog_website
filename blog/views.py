from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.contrib.auth import login, logout

from .models import Category, News, Product_category, Product
from .forms import Login, Register


def index(request):
    categories = Category.objects.all()
    articles = News.objects.all()
    context = {
        'categories': categories,
        'title': 'Birinchi sayt',
        'articles': articles,

    }
    return render(request, template_name= 'blog/index.html', context=context)

def category_list(request, id):
    category = Category.objects.get(pk=id)
    articles = News.objects.filter(category=category)

    context = {
        'title': category.title,
        'category': category,
        'articles': articles,

    }
    return render(request, 'blog/index.html', context)


def article_detail(request, pk):

    article = News.objects.get(pk=pk)
    context ={
        'title': article.title,
        'article': article

    }
    return render(request, 'blog/article_detail.html', context)

def category_detail(request, id):
    category = Product_category.objects.get(pk=id)
    products = Product.objects.filter(category=category)
    return render(request, 'blog/category_detail.html', {'category': category, 'products': products})



def user_login(request):
    if request.method == 'POST':
        form = Login(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = Login()
    context = {
        'title': 'Enter',
        'form': form
    }
    return render(request, 'blog/login_form.html', context)

def register_user(request):
    if request.method == 'POST':
        form = Register(data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('index')
    else:
        form = Register()
    context = {
            'title': 'Registration',
            'form': form
        }
    return render(request, 'blog/register_form.html', context)


def user_logout(request):
    logout(request)
    return redirect('index')
















