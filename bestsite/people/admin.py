from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import *
from people.models import People, Category, CustomUser, Comment

class PeopleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'cat', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create', 'cat')
    prepopulated_fields = {'slug': ('title',)}  # делаем автозаполнение для поля slug полем title в админ панели

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'logo')
    list_display_links = ('id', 'name')
    list_editable = ('logo',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}   # делаем автозаполнение для поля slug полем name в админ панели

class CustomUserAdmin(UserAdmin):
    add_form = RegisterUserForm
    form = ChangeUserForm
    model = CustomUser
    list_display = ('username', 'slug', 'photo', 'context', 'birthday')
    list_editable = ('photo', 'context', 'birthday', 'slug')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'people')
    list_display_links = ('id', 'author')

admin.site.register(People, PeopleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Comment, CommentAdmin)
