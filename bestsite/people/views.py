from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *
from .utils import *


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')

def about(request):
    menu_about = menu.copy()
    if not request.user.is_authenticated:
        menu_about.pop(1)
    context = {'title': 'Страница о нас', 'menu': menu_about}
    return render(request, 'people/about.html', context)

def logout_user(request):
    logout(request)     # стандартная ф-ия джанго для выхода пользователя
    return redirect('main')

# ----------------------------------------------------------------

class HomeListView(DataMixin, ListView):
    model = People
    template_name = 'people/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        c_def = self.get_user_context(title='Все люди')
        context = dict(list(context.items()) + list(c_def.items()))
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

class UserDetailView(DataMixin, DetailView):
    model = CustomUser
    template_name = 'people/u_detail.html'
    context_object_name = 'el'
    slug_url_kwarg = 'user_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = CustomUser.objects.get(slug=self.kwargs['user_slug'])
        c_def = self.get_user_context(title=user.username)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

# ----------------------------------------------------------------

class UserUpdateView(DataMixin, UpdateView):
    model = CustomUser
    form_class = UpdateUserForm
    template_name = 'people/registration.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        c_def = self.get_user_context(title='Edit user')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_success_url(self):
        post = CustomUser.objects.get(slug=self.kwargs['slug'])
        return post.get_absolute_url()

# ----------------------------------------------------------------

class PeopleDetailView(DataMixin, DetailView, CreateView):
    model = People
    form_class = CommentForm
    template_name = 'people/p_detail.html'
    context_object_name = 'el'
    slug_url_kwarg = 'people_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = People.objects.get(slug=self.kwargs['people_slug'])
        comments = Comment.objects.filter(people=post)

        c_def = self.get_user_context(title=context['el'], is_selected=post.cat.pk, comments=comments)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_success_url(self):      # если форма создана идет переадресация
        post = People.objects.get(slug=self.kwargs['people_slug'])
        return post.get_absolute_url()

    def form_valid(self, form):     # если форма коомента валидна то создается коммент где автор текущий пол-ль, а пипл выбранный пост
        form.instance.author = self.request.user
        project = People.objects.get(slug=self.kwargs['people_slug'])
        form.instance.people = project
        return super().form_valid(form)

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

class CommentDeleteView(DataMixin, DeleteView):
    model = Comment
    template_name = 'people/delete_blog.html'
    context_object_name = 'el'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        c_def = self.get_user_context(title='Delete comment')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_success_url(self):
        post = Comment.objects.get(pk=self.kwargs['pk'])
        return post.people.get_absolute_url()

# ----------------------------------------------------------------

class CategoryListView(DataMixin, ListView):
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

        c_def = self.get_user_context(is_selected=cat.pk, title=cat.name)
        context = dict(list(context.items()) + list(c_def.items()))
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

class PeopleCreateView(LoginRequiredMixin, DataMixin, CreateView):
    form_class = PeopleForm
    template_name = 'people/add_article.html'
    success_url = reverse_lazy('main')
    login_url = '/admin/'   # это относится к LoginRequiredMixin, если нет авторизании то идет перенаправление

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Add article')
        return dict(list(context.items()) + list(c_def.items()))

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

class RegisterUser(DataMixin, CreateView):
    # form_class = UserCreationForm     можно напрямую отдать форму от джанго или создать свою в forms.py
    form_class = RegisterUserForm
    template_name = 'people/registration.html'
    success_url = reverse_lazy('main')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):     # эта ф-ия вызывается после успешной обработки формы и залогинивает пол-ля
        user = form.save()
        login(self.request, user)
        return redirect('main')

# ----------------------------------------------------------------

class LoginUser(DataMixin, LoginView):
    # form_class = AuthenticationForm
    form_class = LoginUserForm
    template_name = 'people/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('main')

# ----------------------------------------------------------------

