from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .models import *


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')


def about(request):
    context = {'title': 'About page'}
    return render(request, 'people/about.html', context)

# ----------------------------------------------------------------
class HomeListView(ListView):
    model = People
    template_name = 'people/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'People page'
        context['is_selected'] = 0
        return context

    def get_queryset(self):
        return People.objects.filter(is_published=True)

# def home(request):
#     posts = People.objects.all()
#     context = {
#         'posts': posts,
#         'title': 'People page',
#         'is_selected': 0,
#     }
#     return render(request, 'people/index.html', context)


# ----------------------------------------------------------------
class PeopleDetailView(DetailView):
    model = People
    template_name = 'people/p_detail.html'
    context_object_name = 'el'
    slug_url_kwarg = 'people_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = People.objects.get(slug=self.kwargs['people_slug'])
        context['title'] = 'People detail page'
        context['is_selected'] = post.cat.pk
        return context

# def people_detail(request, people_slug):
#     post = get_object_or_404(People, slug=people_s    lug)
#     cat = post.cat.pk
#     context = {
#         'el': post,
#         'title': 'People detail page',
#         'is_selected': cat
#     }
#     return render(request, 'people/p_detail.html', context)

# ----------------------------------------------------------------
class CategoryListView(ListView):
    model = People
    template_name = 'people/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        # cat = Category.objects.get(slug=self.kwargs['cat_slug'])
        # post = People.objects.filter(cat=cat, is_published=True)
        post = People.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)  # эту строку можно заменить 2мя предыдущими
        if len(post) == 0:
            raise Http404()
        return post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = Category.objects.get(slug=self.kwargs['cat_slug'])
        context['is_selected'] = cat.pk
        context['title'] = cat.name
        return context

# def category(request, cat_slug):
#     cat = Category.objects.get(slug=cat_slug)
#     post = People.objects.filter(cat=cat)
#
#     if len(post) == 0:
#         raise Http404()
#
#     context = {
#         'posts': post,
#         'title': cat.name,
#         'is_selected': cat.pk
#     }
#     return render(request, 'people/index.html', context)
# ----------------------------------------------------------------

class PeopleCreateView(CreateView):
    form_class = PeopleForm
    template_name = 'people/add_article.html'
    success_url = reverse_lazy('main')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add article'
        return context

# def add_article(request):
#     if request.method == 'POST':
#         form = PeopleForm(request.POST, request.FILES)
#         if form.is_valid():
#             try:
#                 # People.objects.create(**form.cleaned_data)
#                 form.save()
#                 return redirect('main')
#             except:
#                 form.add_error(None, 'Error data')  # Создается общая ошибка, если форма не связана с моделью и некорректна
#     else:
#         form = PeopleForm()
#     context = {
#         'form': form,
#         'title': 'Add article',
#     }
#     return render(request, 'people/add_article.html', context)
# ----------------------------------------------------------------
