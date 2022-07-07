from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('', HomeListView.as_view(), name='main'),
    path('about/', about, name='about'),
    path('favorite/<int:pk>', favorite, name='favorite'),
    path('not_favorite/<int:pk>', not_favorite, name='not_favorite'),
    path('logout/', logout_user, name='logout'),
    path('sign_in/', LoginUser.as_view(), name='sign_in'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('my_favorites/', FavoritesListView.as_view(), name='my_favorites'),
    path('add_article/', PeopleCreateView.as_view(), name='add_article'),
    path('user/<slug:user_slug>/', UserDetailView.as_view(), name='user_detail'),
    path('user_edit/<slug:slug>', UserUpdateView.as_view(), name='user_edit'),
    path('people_detail/<slug:people_slug>/', PeopleDetailView.as_view(), name='people_detail'),
    path('delete_people/<int:pk>', PeopleDeleteView.as_view(), name='delete_people'),
    path('delete_comment/<int:pk>', CommentDeleteView.as_view(), name='delete_comment'),
    path('category/<slug:cat_slug>/', CategoryListView.as_view(), name='category')

]
