from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), #(1) use path, (2)define the path in the views file, (3)give it a name
    path('about/', views.about, name='about'),
    path('games/', views.games_index, name='index'),
    path('games/<int:game_id>/', views.games_detail, name='detail'),
    path('games/create', views.GameCreate.as_view(), name='games_create'),
    path('games/<int:pk>/update', views.GameUpdate.as_view(), name='games_update'), #class-based views force you to use PK
    path('games/<int:pk>/delete', views.GameDelete.as_view(), name='games_delete'),
    path('games/<int:game_id>/add_review', views.add_review, name='add_review'),
    path('games/<int:game_id>/assoc_player/<int:player_id>/', views.assoc_player, name='assoc_player'),
    path('games/<int:game_id>/unassoc_player/<int:player_id>/', views.unassoc_player, name='unassoc_player'),
    path('players/', views.PlayerList.as_view(), name='players_index'),
    path('players/<int:pk>/', views.PlayerDetail.as_view(), name='players_detail'),
    path('players/create/', views.PlayerCreate.as_view(), name='players_create'),
    path('players/<int:pk>/update/', views.PlayerUpdate.as_view(), name='players_update'),
    path('players/<int:pk>/delete/', views.PlayerDelete.as_view(), name='players_delete'),
]