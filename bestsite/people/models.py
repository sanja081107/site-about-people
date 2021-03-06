from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe

# ------------------------------------------------------------------------------------------
from bestsite import settings


class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', null=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='URL', null=True)
    context = models.TextField(verbose_name='Краткая информация', null=True)
    birthday = models.DateTimeField(verbose_name='День рождения', null=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_absolute_url(self):
        return reverse('user_detail', kwargs={'user_slug': self.slug})

    def __str__(self):
        return self.username

# ------------------------------------------------------------------------------------------

class People(models.Model):
    title = models.CharField(max_length=50, verbose_name='Имя')
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Контент')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовать')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    author = models.ForeignKey('CustomUser', on_delete=models.PROTECT, verbose_name='Автор')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'People'
        verbose_name_plural = 'Peoples'
        ordering = ['-time_create', 'title']

    def get_absolute_url(self):
        return reverse('people_detail', kwargs={'people_slug': self.slug})

# ------------------------------------------------------------------------------------------

class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='URL')
    logo = models.CharField(max_length=255, verbose_name='logo', null=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    def get_html_logo(self):
        return mark_safe(f'{self.logo}')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['name']

# ------------------------------------------------------------------------------------------

class Comment(models.Model):
    author = models.ForeignKey('CustomUser', on_delete=models.CASCADE, verbose_name='Имя автора')
    people = models.ForeignKey('People', on_delete=models.CASCADE, verbose_name='Имя поста')
    context = models.TextField(max_length=100, verbose_name='Содержание')

    def __str__(self):
        return f'{self.author}'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['pk']

# ------------------------------------------------------------------------------------------

class FavoritesPeople(models.Model):
    author = models.ForeignKey('CustomUser', on_delete=models.CASCADE, verbose_name='Имя автора')
    people = models.ForeignKey('People', on_delete=models.CASCADE, verbose_name='Имя поста')

    def __str__(self):
        return f'{self.people}'

    class Meta:
        verbose_name = 'Favorite'
        verbose_name_plural = 'Favorites'
        ordering = ['pk']

# ------------------------------------------------------------------------------------------
