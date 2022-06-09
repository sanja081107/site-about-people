from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('', cache_page(30)(HomeListView.as_view()), name='main'),
    path('about/', about, name='about'),
    path('logout/', logout_user, name='logout'),
    path('sign_in/', LoginUser.as_view(), name='sign_in'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('add_article/', PeopleCreateView.as_view(), name='add_article'),
    path('user/<slug:user_slug>/', UserDetailView.as_view(), name='user_detail'),
    path('user_edit/<slug:slug>', UserUpdateView.as_view(), name='user_edit'),
    path('people/<slug:people_slug>/', PeopleDetailView.as_view(), name='people_detail'),
    path('delete_comment/<int:pk>', CommentDeleteView.as_view(), name='delete_comment'),
    path('category/<slug:cat_slug>/', cache_page(60)(CategoryListView.as_view()), name='category')

]
