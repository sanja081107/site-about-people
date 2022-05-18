from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .forms import *
from .models import *


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


def people_detail(request, people_slug):
    post = get_object_or_404(People, slug=people_slug)
    cat = post.cat.pk
    context = {
        'el': post,
        'title': 'People detail page',
        'is_selected': cat
    }
    return render(request, 'people/p_detail.html', context)


def category(request, cat_slug):
    cat = Category.objects.get(slug=cat_slug)
    post = People.objects.filter(cat=cat)

    if len(post) == 0:
        raise Http404()

    context = {
        'posts': post,
        'title': cat.name,
        'is_selected': cat.pk
    }
    return render(request, 'people/index.html', context)


def add_article(request):
    if request.method == 'POST':
        form = PeopleForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                # People.objects.create(**form.cleaned_data)
                form.save()
                return redirect('main')
            except:
                form.add_error(None, 'Error data')  # Создается общая ошибка, если форма не связана с моделью и некорректна
    else:
        form = PeopleForm()
    context = {
        'form': form,
        'title': 'Add article',
    }
    return render(request, 'people/add_article.html', context)
