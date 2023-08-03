from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Game, Player
from .forms import ReviewForm


# games = [
#     {'name': 'The Witcher 3: Enhanced Edition', 'genre': 'RPG', 'release_date': '2015-05-15', 'in_library': True},
#     {'name': 'XCOM 2', 'genre': 'Strategy', 'release_date': '2016-02-05', 'in_library': True},
#     {'name': 'Total War: Three Kingdoms', 'genre': 'Strategy', 'release_date': '2019-05-23', 'in_library': True},
#     {'name': 'Stardew Valley', 'genre': 'Simulation', 'release_date': '2016-02-26', 'in_library': True},
#     {'name': 'Star Wars Jedi: Fallen Order', 'genre': 'Action-Adventure', 'release_date': '22019-11-15', 'in_library': True},
#     {'name': 'Elden Ring', 'genre': 'Souls-like', 'release_date': '2022-02-24', 'in_library': False},
#     {'name': 'Red-Dead Redemption 2', 'genre': 'Action-Adventure', 'release_date': '2019-12-05', 'in_library': False},
# ]

# Create your views here.
def home (request): #(4) define it in the views file. request is standard
    return render (request, 'home.html') #(5) render teh page upon request, send it to the html page in the 'templates' folder

def about (request):
    return render (request, 'about.html')

def games_index (request):
    games = Game.objects.all()
    return render (request, 'games/index.html', {
        'games': games,
    })

def games_detail (request, game_id):
    game = Game.objects.get(id=game_id)
    id_list = game.players.all().values_list('id')
    available_players = Player.objects.exclude(id__in=id_list)
    #instantiate ReviewForm to be rendered in detail.html
    review_form = ReviewForm()
    return render (request, 'games/detail.html', {
        'game': game,
        'review_form': review_form,
        'available_players': available_players,
    })

# Create a class to be applied to a specific model
class GameCreate(CreateView):
    model = Game
    fields = ['name', 'genre', 'release_date', 'description'] #displays only the name and age field in the form
    #fields = '__all__' #displays all field in the form

class GameUpdate(UpdateView):
    model = Game
    fields = '__all__'

class GameDelete(DeleteView):
    model = Game
    success_url = '/games'

def add_review(request, game_id):
    #create a ModelForm instance using the data that was submitted in the form
    form = ReviewForm(request.POST) #««« this is how te tell it that we will use the information passed on by the 'form' in the html
    #validate the form
    if form.is_valid():
        # We want a model instance, but we can't save to the database yet
        # because we have not yet assigned the game_id FK.
        new_review = form.save(commit=False)
        new_review.game_id = game_id
        new_review.save()
    return redirect('detail', game_id=game_id) #redirect takes advantage of the 'name' property in the routes, so we can use that instead of passing the entire route

class PlayerList(ListView):
    model = Player

class PlayerDetail(DetailView):
    model = Player

class PlayerCreate(CreateView):
    model = Player
    fields = '__all__'

class PlayerUpdate(UpdateView):
    model = Player
    fields = '__all__'

class PlayerDelete(DeleteView):
    model = Player
    success_url = '/players'

def assoc_player(request, game_id, player_id):
  Game.objects.get(id=game_id).players.add(player_id)
  return redirect('detail', game_id=game_id)

def unassoc_player(request, game_id, player_id):
  Game.objects.get(id=game_id).players.remove(player_id)
  return redirect('detail', game_id=game_id)

