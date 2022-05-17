from django import template
from people.models import *

register = template.Library()

@register.simple_tag(name='getcats')
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('people/list_categories.html')
def show_categories(sort=None, is_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)
    return {'cats': cats, 'is_selected': is_selected}
