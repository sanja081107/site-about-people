from django.contrib import admin

from people.models import People, Category

class PeopleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'cat', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create', 'cat')
    prepopulated_fields = {'slug': ('title',)}  # делаем автозаполнение для поля slug полем title в админ панели

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}   # делаем автозаполнение для поля slug полем name в админ панели

admin.site.register(People, PeopleAdmin)
admin.site.register(Category, CategoryAdmin)
