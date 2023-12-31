# Generated by Django 4.2.3 on 2023-08-03 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_game_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(choices=[('5', 'Excelent'), ('4', 'Great'), ('3', 'Average'), ('2', 'Okay'), ('1', 'Awful')], default=2, max_length=1)),
                ('title', models.CharField(max_length=100)),
                ('review', models.TextField(max_length=250)),
                ('date', models.DateField(verbose_name='posted on')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.game')),
            ],
        ),
    ]
