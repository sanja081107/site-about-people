from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import People, Category

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')

def home(request):
    posts = People.objects.all()
    context = {
        'posts': posts,
        'title': 'People page',
        'is_selected': 0,
    }
    return render(request, 'people/index.html', context)

def about(request):
    context = {'title': 'About page'}
    return render(request, 'people/about.html', context)

def people_detail(request, people_id):
    post = People.objects.get(pk=people_id)
    cat = post.cat.pk
    context = {
        'el': post,
        'title': 'People detail page',
        'is_selected': cat
    }
    return render(request, 'people/p_detail.html', context)

def category(request, cat_id):
    post = People.objects.filter(cat_id=cat_id)

    if len(post) == 0:
        raise Http404()

    context = {
        'posts': post,
        'title': 'People detail page',
        'is_selected': cat_id
    }
    return render(request, 'people/index.html', context)
