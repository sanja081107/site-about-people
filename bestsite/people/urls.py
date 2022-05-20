from django.urls import path

from .views import *

urlpatterns = [
    path('', HomeListView.as_view(), name='main'),
    path('about/', about, name='about'),
    path('sign_in/', HomeListView.as_view(), name='sign_in'),
    path('add_article/', PeopleCreateView.as_view(), name='add_article'),
    path('people/<slug:people_slug>/', PeopleDetailView.as_view(), name='people_detail'),
    path('category/<slug:cat_slug>/', CategoryListView.as_view(), name='category')

]
