# Generated by Django 4.2.3 on 2023-08-03 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_player_alter_review_options_alter_game_in_library'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='player',
            field=models.ManyToManyField(to='main_app.player'),
        ),
    ]