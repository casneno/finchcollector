from django.db import models
from django.urls import reverse
from datetime import date

#define RATINGS tuple, with nested 2-tuples
RATINGS = (
    ('5', 'Excelent'),
    ('4', 'Great'),
    ('3', 'Average'),
    ('2', 'Okay'),
    ('1', 'Awful'),
)

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=50)
    online = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('players_detail', kwargs={'pk': self.id})
    


class Game(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    release_date = models.DateField()
    description = models.TextField(max_length=300, default='')
    in_library = models.BooleanField(default=False)
    players = models.ManyToManyField(Player)

    def __str__(self):
        return f'Game is {self.name}, {self.release_date}'
    
# Automatically redirects to the game details page upon game creation
    def get_absolute_url(self):
        return reverse('detail', kwargs={'game_id': self.id})
    
# Detect if the game is hungry or not
    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(RATINGS)   



class Review(models.Model):
    rating = models.CharField(max_length=1, choices = RATINGS, default = [2][0])
    title = models.CharField(max_length=100)
    review = models.TextField(max_length=250)
    date = models.DateField('posted on')

    #create a game_id FK, since Review belongs to Game
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.get_rating_display()} - {self.title}: {self.review} - reviewed on {self.date}"
    
    class Meta: #a Meta class doesn't affect the class's structure
        ordering = ['-date'] #order indorfation in descending order by date