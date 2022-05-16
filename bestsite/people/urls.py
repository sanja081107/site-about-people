from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='main'),
    path('about/', about, name='about'),
    path('sign_in/', home, name='sign_in'),
    path('people/<int:people_id>/', people_detail, name='people_detail'),
    path('category/<int:cat_id>/', category, name='category')

]
