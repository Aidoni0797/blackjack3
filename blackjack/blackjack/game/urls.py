from django.urls import path
from .views import *

app_name = 'game'

urlpatterns = [
    path('', index, name='index'),
    path('login_player/', login_player, name='login_player'),
    path('start_game/', start_game, name='start_game'),
    path('game/<int:id>/', show_game, name='show_game'),
    path('add_card/', add_card, name='add_card'),
    path('register_player/', register_player, name='register_player'),
]
