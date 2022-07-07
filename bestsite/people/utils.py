from .models import *

menu = [{'title': 'Главная', 'url_name': 'main'},
        {'title': 'Добавить статью', 'url_name': 'add_article'},
        {'title': 'Избранное', 'url_name': 'my_favorites'},
        {'title': 'Обо мне', 'url_name': 'about'}]

class DataMixin:
    paginate_by = 2

    def get_user_context(self, **kwargs):
        context = kwargs
        user_menu = menu.copy()

        if not self.request.user.is_authenticated:
            user_menu.pop(1)
            user_menu.pop(1)
        else:
            favorites = FavoritesPeople.objects.filter(author=self.request.user)
            context['favorites_len'] = len(favorites)

        context['menu'] = user_menu

        if 'is_selected' not in context:
            context['is_selected'] = 0

        return context
