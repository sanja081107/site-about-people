from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Room, Message

# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_html_value', 'user', 'room')
    list_display_links = ('id', 'get_html_value',)

    def get_html_value(self, object):
        if object.value:
            return mark_safe(f'<p>{ object.value[:7] }...<p/>')
    get_html_value.short_description = 'Message'

admin.site.register(Room, RoomAdmin)
admin.site.register(Message, MessageAdmin)
