from django.urls import path
from .views import *

urlpatterns = [
    path('chat/', home, name='forum'),
    path('<int:pk>/', input_name, name='input_name'),
    path('<str:room>/', room, name='room'),
    path('checkview', checkview, name='checkview'),
    path('send', send, name='send'),
    path('getMessages/<str:room>/', getMessages, name='getMessages'),
]