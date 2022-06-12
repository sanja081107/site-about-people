from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import *
from people.models import People, Category, CustomUser, Comment

class PeopleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'cat', 'time_create', 'get_html_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create', 'cat')
    prepopulated_fields = {'slug': ('title',)}  # делаем автозаполнение для поля slug полем title в админ панели
    fields = ('title', 'slug', 'content', 'cat', 'time_create', 'time_update', 'get_html_photo', 'photo', 'is_published')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{ object.photo.url }' width=50>")

    get_html_photo.short_description = 'Миниатюра'

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
    list_display = ('username', 'get_html_photo', 'photo', 'context', 'slug', 'birthday')
    list_editable = ('photo', 'context', 'birthday', 'slug')

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{ object.photo.url }' width=50>")

    get_html_photo.short_description = 'Миниатюра'

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'people', 'context')
    list_display_links = ('id', 'author')

admin.site.register(People, PeopleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Comment, CommentAdmin)

admin.site.site_title = 'Site about people'
admin.site.site_header = 'Site about people'
admin.site.index_title = 'Admin'
