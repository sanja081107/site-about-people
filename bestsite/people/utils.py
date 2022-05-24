from .models import *

menu = [{'title': 'Main', 'url_name': 'main'},
        {'title': 'Add article', 'url_name': 'add_article'},
        {'title': 'About', 'url_name': 'about'}]

class DataMixin:
    paginate_by = 2

    def get_user_context(self, **kwargs):
        context = kwargs
        user_menu = menu.copy()

        if not self.request.user.is_authenticated:
            user_menu.pop(1)
        context['menu'] = user_menu

        if 'is_selected' not in context:
            context['is_selected'] = 0

        return context
