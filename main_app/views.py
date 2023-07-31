from django.shortcuts import render

games = [
    {'name': 'The Witcher 3: Enhanced Edition', 'genre': 'RPG', 'release_date': '2015-05-15', 'in_library': True},
    {'name': 'XCOM 2', 'genre': 'Strategy', 'release_date': '2016-02-05', 'in_library': True},
    {'name': 'Total War: Three Kingdoms', 'genre': 'Strategy', 'release_date': '2019-05-23', 'in_library': True},
    {'name': 'Stardew Valley', 'genre': 'Simulation', 'release_date': '2016-02-26', 'in_library': True},
    {'name': 'Star Wars Jedi: Fallen Order', 'genre': 'Action-Adventure', 'release_date': '22019-11-15', 'in_library': True},
    {'name': 'Elden Ring', 'genre': 'Souls-like', 'release_date': '2022-02-24', 'in_library': False},
    {'name': 'Red-Dead Redemption 2', 'genre': 'Action-Adventure', 'release_date': '2019-12-05', 'in_library': False},
]

# Create your views here.
def home (request):
    return render (request, 'home.html')

def about (request):
    return render (request, 'about.html')

def games_index (request):
    return render (request, 'games/index.html', {
        'games': games,
    })

def games_details (request):
    return render (request, 'games/details.html', {
        'game': games,
    })
