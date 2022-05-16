from django.db import models
from django.urls import reverse


class People(models.Model):
    title = models.CharField(max_length=50, verbose_name='Имя')
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'people'
        verbose_name_plural = 'peoples'
        ordering = ['-time_create', 'title']

    def get_absolute_url(self):
        return reverse('people_detail', kwargs={'people_id': self.pk})

class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Название')

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['name']
