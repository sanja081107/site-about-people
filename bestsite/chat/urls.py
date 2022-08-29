from django.urls import path
from .views import *

urlpatterns = [
    path('chat/', home, name='forum'),
    path('<int:pk>/', input_name, name='input_name'),
    path('<int:pk>-chat/', room, name='room'),
    path('delete_chat/<int:pk>', delete_chat, name='delete_chat'),
    path('checkview', checkview, name='checkview'),
    path('send', send, name='send'),
    path('getMessages/<int:pk>/', getMessages, name='getMessages'),
]