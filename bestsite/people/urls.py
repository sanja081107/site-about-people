from django.urls import path

from .views import *

urlpatterns = [
    path('', HomeListView.as_view(), name='main'),
    path('about/', about, name='about'),
    path('logout/', logout_user, name='logout'),
    path('sign_in/', LoginUser.as_view(), name='sign_in'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('add_article/', PeopleCreateView.as_view(), name='add_article'),
    path('user/<slug:user_slug>/', UserDetailView.as_view(), name='user_detail'),
    path('people/<slug:people_slug>/', PeopleDetailView.as_view(), name='people_detail'),
    path('category/<slug:cat_slug>/', CategoryListView.as_view(), name='category')

]
