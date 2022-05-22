from django import template
from django.db.models import Count

from people.models import *

register = template.Library()

@register.simple_tag(name='getcats')
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('people/list_categories.html')
def show_categories(sort=None, is_selected=0):
    if not sort:
        cats = Category.objects.all()
        cats = cats.annotate(Count('people'))
    else:
        cats = Category.objects.order_by(sort)
        cats = cats.annotate(Count('people'))
    return {'cats': cats, 'is_selected': is_selected}
