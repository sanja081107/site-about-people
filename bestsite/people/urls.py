from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='main'),
    path('about/', about, name='about'),
    path('sign_in/', home, name='sign_in'),
    path('people/<slug:people_slug>/', people_detail, name='people_detail'),
    path('category/<slug:cat_slug>/', category, name='category')

]
